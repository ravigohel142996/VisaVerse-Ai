"""
Visa Service - Handles all visa-related logic and recommendations
"""

import json
import os


class VisaService:
    def __init__(self):
        """Initialize the visa service with data from JSON file"""
        self.data = self._load_visa_data()
    
    def _load_visa_data(self):
        """Load visa rules from JSON file"""
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'visa_rules.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_visa_recommendations(self, profile):
        """
        Get visa recommendations based on user profile
        
        Args:
            profile (dict): User profile containing:
                - citizenship: str
                - destination: str
                - purpose: str (Work/Employment, Study, Tourism, Business, etc.)
                - education: str
                - work_experience: int (years)
                - job_title: str (optional)
        
        Returns:
            list: List of recommended visa options with details
        """
        purpose = profile.get('purpose', '')
        destination = profile.get('destination', '')
        education = profile.get('education', '')
        work_experience = profile.get('work_experience', 0)
        
        recommendations = []
        
        # Map purpose to visa types
        if purpose == 'Work/Employment':
            # Skilled worker visa
            if 'skilled_worker' in self.data['visa_types']:
                visa = self.data['visa_types']['skilled_worker']
                if destination in visa['countries']:
                    score = self._calculate_eligibility_score(profile, visa)
                    recommendations.append({
                        'name': visa['name'],
                        'processing_time': visa['processing_time'],
                        'validity': visa['validity'],
                        'requirements': visa['requirements'],
                        'eligibility_score': score,
                        'success_rate': self._get_success_rate(score)
                    })
            
            # Intra-company transfer
            if 'intra_company_transfer' in self.data['visa_types']:
                visa = self.data['visa_types']['intra_company_transfer']
                if destination in visa['countries']:
                    recommendations.append({
                        'name': visa['name'],
                        'processing_time': visa['processing_time'],
                        'validity': visa['validity'],
                        'requirements': visa['requirements'],
                        'eligibility_score': 85,
                        'success_rate': 'Very High'
                    })
        
        elif purpose == 'Study':
            if 'student' in self.data['visa_types']:
                visa = self.data['visa_types']['student']
                if destination in visa['countries']:
                    score = self._calculate_eligibility_score(profile, visa)
                    recommendations.append({
                        'name': visa['name'],
                        'processing_time': visa['processing_time'],
                        'validity': visa['validity'],
                        'requirements': visa['requirements'],
                        'eligibility_score': score,
                        'success_rate': self._get_success_rate(score)
                    })
        
        elif purpose == 'Business':
            if 'business' in self.data['visa_types']:
                visa = self.data['visa_types']['business']
                if destination in visa['countries']:
                    recommendations.append({
                        'name': visa['name'],
                        'processing_time': visa['processing_time'],
                        'validity': visa['validity'],
                        'requirements': visa['requirements'],
                        'eligibility_score': 80,
                        'success_rate': 'High'
                    })
        
        else:  # Tourism, Family, Other
            if 'tourist' in self.data['visa_types']:
                visa = self.data['visa_types']['tourist']
                if destination in visa['countries']:
                    recommendations.append({
                        'name': visa['name'],
                        'processing_time': visa['processing_time'],
                        'validity': visa['validity'],
                        'requirements': visa['requirements'],
                        'eligibility_score': 75,
                        'success_rate': 'High'
                    })
        
        return recommendations
    
    def _calculate_eligibility_score(self, profile, visa_type):
        """
        Calculate eligibility score based on profile and visa requirements
        
        Args:
            profile (dict): User profile
            visa_type (dict): Visa type information
        
        Returns:
            int: Eligibility score (0-100)
        """
        score = 50  # Base score
        
        # Education points
        education = profile.get('education', '')
        if education in self.data['eligibility_criteria']['education_points']:
            score += self.data['eligibility_criteria']['education_points'][education] * 0.5
        
        # Experience points
        work_experience = profile.get('work_experience', 0)
        exp_category = self._categorize_experience(work_experience)
        if exp_category in self.data['eligibility_criteria']['experience_points']:
            score += self.data['eligibility_criteria']['experience_points'][exp_category] * 0.5
        
        # Cap at 100
        return min(int(score), 100)
    
    def _categorize_experience(self, years):
        """Categorize work experience into ranges"""
        if years <= 2:
            return '0-2'
        elif years <= 5:
            return '3-5'
        elif years <= 10:
            return '6-10'
        elif years <= 15:
            return '11-15'
        else:
            return '16+'
    
    def _get_success_rate(self, score):
        """Convert eligibility score to success rate description"""
        if score >= 85:
            return 'Very High'
        elif score >= 70:
            return 'High'
        elif score >= 55:
            return 'Moderate'
        else:
            return 'Low'
    
    def get_country_info(self, country):
        """
        Get country-specific visa information
        
        Args:
            country (str): Country name
        
        Returns:
            dict: Country-specific visa information
        """
        if country in self.data['country_specific_info']:
            return self.data['country_specific_info'][country]
        return None
    
    def get_all_countries(self):
        """Get list of all countries with visa information"""
        return list(self.data['country_specific_info'].keys())
    
    def get_visa_types_for_country(self, country):
        """Get available visa types for a specific country"""
        visa_types = []
        for visa_key, visa_data in self.data['visa_types'].items():
            if country in visa_data['countries']:
                visa_types.append(visa_data['name'])
        return visa_types

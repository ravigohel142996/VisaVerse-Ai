"""
Document Service - Handles document checking and readiness validation
"""

from utils.constants import MIN_RESUME_LENGTH, MIN_OFFER_LENGTH


class DocumentService:
    def __init__(self):
        """Initialize the document service"""
        self.document_requirements = self._load_document_requirements()
    
    def _load_document_requirements(self):
        """Load document requirements for different visa types"""
        return {
            'Skilled Worker': {
                'essential': [
                    'Valid passport (minimum 6 months validity)',
                    'Recent passport-sized photographs',
                    'Completed visa application form',
                    'Visa application fee payment receipt'
                ],
                'specific': [
                    'Certificate of Sponsorship from employer',
                    'Proof of financial means',
                    'Educational certificates and transcripts',
                    'Work experience letters',
                    'English language test results (IELTS/TOEFL)'
                ]
            },
            'Student': {
                'essential': [
                    'Valid passport (minimum 6 months validity)',
                    'Recent passport-sized photographs',
                    'Completed visa application form',
                    'Visa application fee payment receipt'
                ],
                'specific': [
                    'University acceptance letter',
                    'Proof of tuition fees and living expenses',
                    'Previous academic records',
                    'English language proficiency test'
                ]
            },
            'Tourist': {
                'essential': [
                    'Valid passport (minimum 6 months validity)',
                    'Recent passport-sized photographs',
                    'Completed visa application form',
                    'Visa application fee payment receipt'
                ],
                'specific': [
                    'Travel itinerary',
                    'Hotel bookings or invitation letter',
                    'Bank statements (last 3 months)'
                ]
            },
            'Business': {
                'essential': [
                    'Valid passport (minimum 6 months validity)',
                    'Recent passport-sized photographs',
                    'Completed visa application form',
                    'Visa application fee payment receipt'
                ],
                'specific': [
                    'Business invitation letter',
                    'Company registration documents',
                    'Proof of financial stability'
                ]
            }
        }
    
    def get_required_documents(self, visa_type):
        """
        Get list of required documents for a visa type
        
        Args:
            visa_type (str): Type of visa
        
        Returns:
            dict: Dictionary with 'essential' and 'specific' document lists
        """
        if visa_type in self.document_requirements:
            return self.document_requirements[visa_type]
        return {'essential': [], 'specific': []}
    
    def calculate_readiness_score(self, visa_type, checked_documents):
        """
        Calculate document readiness score
        
        Args:
            visa_type (str): Type of visa
            checked_documents (dict): Dictionary of document name -> boolean (checked or not)
        
        Returns:
            dict: Readiness information including score and missing documents
        """
        requirements = self.get_required_documents(visa_type)
        all_docs = requirements['essential'] + requirements['specific']
        total_docs = len(all_docs)
        
        if total_docs == 0:
            return {
                'score': 0,
                'percentage': 0,
                'total': 0,
                'completed': 0,
                'missing': []
            }
        
        completed = sum(1 for doc in all_docs if checked_documents.get(doc, False))
        percentage = (completed / total_docs) * 100
        missing = [doc for doc in all_docs if not checked_documents.get(doc, False)]
        
        return {
            'score': int(percentage),
            'percentage': percentage,
            'total': total_docs,
            'completed': completed,
            'missing': missing
        }
    
    def check_passport_validity(self, expiry_months):
        """
        Check if passport meets validity requirements
        
        Args:
            expiry_months (int): Months until passport expiry
        
        Returns:
            dict: Validity check result
        """
        if expiry_months >= 6:
            return {
                'valid': True,
                'message': 'Your passport meets the minimum validity requirement.',
                'recommendation': None
            }
        elif expiry_months >= 3:
            return {
                'valid': True,
                'message': 'Your passport is valid, but consider renewing soon.',
                'recommendation': 'Some countries require 6 months validity. Consider renewing your passport.'
            }
        else:
            return {
                'valid': False,
                'message': 'Your passport does not meet validity requirements.',
                'recommendation': 'You must renew your passport before applying for a visa.'
            }
    
    def analyze_resume(self, resume_text):
        """
        Analyze resume/CV for completeness
        
        Args:
            resume_text (str): Resume text content
        
        Returns:
            dict: Analysis results
        """
        if not resume_text or len(resume_text.strip()) < MIN_RESUME_LENGTH:
            return {
                'score': 0,
                'issues': ['Resume is too short or empty'],
                'suggestions': ['Include your work experience, education, and skills']
            }
        
        # Simple keyword checks
        issues = []
        suggestions = []
        score = 50  # Base score
        
        # Check for key sections
        resume_lower = resume_text.lower()
        
        if 'experience' in resume_lower or 'work history' in resume_lower:
            score += 15
        else:
            issues.append('Work experience section not found')
            suggestions.append('Add a clear work experience section')
        
        if 'education' in resume_lower or 'university' in resume_lower or 'degree' in resume_lower:
            score += 15
        else:
            issues.append('Education section not found')
            suggestions.append('Add your educational qualifications')
        
        if 'skill' in resume_lower:
            score += 10
        else:
            suggestions.append('Consider adding a skills section')
        
        if '@' in resume_text:  # Email present
            score += 5
        else:
            issues.append('Contact email not found')
            suggestions.append('Add your contact email')
        
        if any(char.isdigit() for char in resume_text):  # Likely has phone number or dates
            score += 5
        
        return {
            'score': min(score, 100),
            'issues': issues if issues else ['No major issues found'],
            'suggestions': suggestions if suggestions else ['Resume looks good!']
        }
    
    def analyze_offer_letter(self, offer_text):
        """
        Analyze job offer letter for key information
        
        Args:
            offer_text (str): Offer letter text content
        
        Returns:
            dict: Analysis results
        """
        if not offer_text or len(offer_text.strip()) < MIN_OFFER_LENGTH:
            return {
                'score': 0,
                'issues': ['Offer letter is too short or empty'],
                'suggestions': ['Ensure you have the complete offer letter']
            }
        
        issues = []
        suggestions = []
        score = 50
        
        offer_lower = offer_text.lower()
        
        # Check for key elements
        if 'salary' in offer_lower or 'compensation' in offer_lower or '$' in offer_text:
            score += 15
        else:
            issues.append('Salary information not clearly mentioned')
            suggestions.append('Ensure salary/compensation is clearly stated')
        
        if 'position' in offer_lower or 'title' in offer_lower or 'role' in offer_lower:
            score += 15
        else:
            issues.append('Job title/position not clearly mentioned')
            suggestions.append('Ensure job title is clearly stated')
        
        if 'start' in offer_lower or 'date' in offer_lower:
            score += 10
        else:
            suggestions.append('Start date should be clearly mentioned')
        
        if 'company' in offer_lower or 'organization' in offer_lower:
            score += 5
        
        if 'sign' in offer_lower or 'signature' in offer_lower:
            score += 5
        else:
            suggestions.append('Ensure the letter is signed by authorized personnel')
        
        return {
            'score': min(score, 100),
            'issues': issues if issues else ['No major issues found'],
            'suggestions': suggestions if suggestions else ['Offer letter looks good!']
        }

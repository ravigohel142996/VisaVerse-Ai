"""
Culture Service - Handles cultural guidance and communication tips
"""

import json
import os


class CultureService:
    def __init__(self):
        """Initialize the culture service with data from JSON file"""
        self.data = self._load_culture_data()
    
    def _load_culture_data(self):
        """Load culture data from JSON file"""
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'culture_data.json')
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Culture data file not found at {data_path}. Please ensure data/culture_data.json exists.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in culture data file: {e}")
    
    def get_country_culture(self, country):
        """
        Get comprehensive cultural information for a country
        
        Args:
            country (str): Country name
        
        Returns:
            dict: Cultural information including workplace, communication, etiquette
        """
        if country in self.data['countries']:
            return self.data['countries'][country]
        return None
    
    def get_workplace_culture(self, country):
        """
        Get workplace culture information for a country
        
        Args:
            country (str): Country name
        
        Returns:
            dict: Workplace culture details
        """
        country_data = self.get_country_culture(country)
        if country_data:
            return country_data.get('workplace_culture', {})
        return {}
    
    def get_communication_style(self, country):
        """
        Get communication style information for a country
        
        Args:
            country (str): Country name
        
        Returns:
            dict: Communication style details
        """
        country_data = self.get_country_culture(country)
        if country_data:
            return country_data.get('communication_style', {})
        return {}
    
    def get_business_etiquette(self, country):
        """
        Get business etiquette information for a country
        
        Args:
            country (str): Country name
        
        Returns:
            dict: Business etiquette details
        """
        country_data = self.get_country_culture(country)
        if country_data:
            return country_data.get('business_etiquette', {})
        return {}
    
    def get_cultural_tips(self, country):
        """
        Get cultural tips for a country
        
        Args:
            country (str): Country name
        
        Returns:
            list: List of cultural tips
        """
        country_data = self.get_country_culture(country)
        if country_data:
            return country_data.get('tips', [])
        return []
    
    def get_time_zone_info(self, country):
        """
        Get time zone information for a country
        
        Args:
            country (str): Country name
        
        Returns:
            str: Time zone information
        """
        country_data = self.get_country_culture(country)
        if country_data:
            return country_data.get('time_zone', 'Not available')
        return 'Not available'
    
    def get_working_hours(self, country):
        """
        Get typical working hours for a country
        
        Args:
            country (str): Country name
        
        Returns:
            str: Working hours information
        """
        country_data = self.get_country_culture(country)
        if country_data:
            return country_data.get('working_hours', 'Not available')
        return 'Not available'
    
    def get_holidays(self, country):
        """
        Get major holidays for a country
        
        Args:
            country (str): Country name
        
        Returns:
            list: List of major holidays
        """
        country_data = self.get_country_culture(country)
        if country_data:
            return country_data.get('holidays', [])
        return []
    
    def get_email_etiquette(self):
        """
        Get general email etiquette guidelines
        
        Returns:
            dict: Email etiquette guidelines
        """
        return self.data.get('general_tips', {}).get('email_etiquette', {})
    
    def get_virtual_meeting_tips(self):
        """
        Get virtual meeting tips
        
        Returns:
            list: List of virtual meeting tips
        """
        return self.data.get('general_tips', {}).get('virtual_meeting_tips', [])
    
    def get_cultural_adaptation_tips(self):
        """
        Get cultural adaptation tips
        
        Returns:
            list: List of cultural adaptation tips
        """
        return self.data.get('general_tips', {}).get('cultural_adaptation', [])
    
    def get_available_countries(self):
        """
        Get list of countries with cultural information
        
        Returns:
            list: List of country names
        """
        return list(self.data['countries'].keys())
    
    def compare_communication_styles(self, country1, country2):
        """
        Compare communication styles between two countries
        
        Args:
            country1 (str): First country name
            country2 (str): Second country name
        
        Returns:
            dict: Comparison of communication styles
        """
        style1 = self.get_communication_style(country1)
        style2 = self.get_communication_style(country2)
        
        return {
            'country1': {
                'name': country1,
                'style': style1
            },
            'country2': {
                'name': country2,
                'style': style2
            }
        }

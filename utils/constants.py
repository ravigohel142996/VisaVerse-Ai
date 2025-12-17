"""
Constants used throughout the VisaVerse Copilot application
"""

# Application metadata
APP_NAME = "VisaVerse Copilot"
APP_VERSION = "1.0.0"
APP_ICON = "✈️"

# Page names
PAGE_HOME = "Home"
PAGE_VISA = "Visa Assistant"
PAGE_DOCUMENTS = "Document Checker"
PAGE_CULTURE = "Cultural Guide"

PAGES = [PAGE_HOME, PAGE_VISA, PAGE_DOCUMENTS, PAGE_CULTURE]

# Countries
COUNTRIES = [
    "Select...",
    "United States",
    "United Kingdom",
    "Canada",
    "Australia",
    "Germany",
    "Japan",
    "India",
    "France",
    "Singapore",
    "Other"
]

# Travel purposes
TRAVEL_PURPOSES = [
    "Select...",
    "Work/Employment",
    "Study",
    "Business",
    "Tourism",
    "Family",
    "Other"
]

# Education levels
EDUCATION_LEVELS = [
    "Select...",
    "High School",
    "Bachelor's Degree",
    "Master's Degree",
    "PhD",
    "Other"
]

# Visa types
VISA_TYPES = [
    "Select...",
    "Skilled Worker",
    "Student",
    "Tourist",
    "Business",
    "Family",
    "Other"
]

# Colors
COLOR_PRIMARY = "#0066ff"
COLOR_SUCCESS = "#00cc66"
COLOR_WARNING = "#ffb700"
COLOR_ERROR = "#ff3333"
COLOR_INFO = "#0099ff"

# Styling
MAX_CONTENT_WIDTH = "900px"
CARD_BORDER_RADIUS = "12px"
CARD_SHADOW = "0 1px 3px rgba(0,0,0,0.08)"
CARD_PADDING = "2rem"

# Messages
DISCLAIMER_TEXT = """⚠️ **Disclaimer:** VisaVerse Copilot provides general information and guidance only. 
This is not legal advice. Visa requirements and policies change frequently. 
Always verify information with official government sources and consult with qualified immigration professionals 
for your specific situation."""

FOOTER_TEXT = "© 2024 VisaVerse Copilot. Built for the VisaVerse AI Hackathon."

# Validation
MIN_RESUME_LENGTH = 100
MIN_OFFER_LENGTH = 100
MIN_PASSPORT_VALIDITY_MONTHS = 6

# Success rate thresholds
VERY_HIGH_THRESHOLD = 85
HIGH_THRESHOLD = 70
MODERATE_THRESHOLD = 55

# Document readiness thresholds
EXCELLENT_READINESS = 90
GOOD_READINESS = 70
FAIR_READINESS = 50

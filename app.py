"""
VisaVerse Copilot - AI-powered assistant for global mobility and visa applications
A clean, minimal Streamlit web app for visa assistance, document checking, and cultural guidance.
"""

import streamlit as st
from services.visa_service import VisaService
from services.document_service import DocumentService
from services.culture_service import CultureService
from utils.constants import *
from utils.helpers import format_requirements_list, get_readiness_message, get_success_rate_emoji

# Initialize services
@st.cache_resource
def get_visa_service():
    return VisaService()

@st.cache_resource
def get_document_service():
    return DocumentService()

@st.cache_resource
def get_culture_service():
    return CultureService()

visa_service = get_visa_service()
document_service = get_document_service()
culture_service = get_culture_service()

# Page configuration
st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for clean, professional styling
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background-color: #fafafa;
    }
    
    /* Center content with max-width */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Card styling */
    .card {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
    }
    
    /* Hero section */
    .hero {
        text-align: center;
        padding: 2.5rem 1rem;
        margin-bottom: 2rem;
    }
    
    .hero h1 {
        font-size: 2.5rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }
    
    .hero p {
        font-size: 1.2rem;
        color: #666;
        margin-top: 0.5rem;
    }
    
    /* Section headings */
    h2 {
        color: #1a1a1a;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #333;
        font-weight: 500;
        margin-bottom: 0.75rem;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: white;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #0066ff;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        border: none;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    
    .stButton > button:hover {
        background-color: #0052cc;
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    
    /* Disclaimer */
    .disclaimer {
        background-color: #fff9e6;
        border-left: 4px solid #ffb700;
        padding: 1rem;
        border-radius: 4px;
        margin-top: 2rem;
        font-size: 0.9rem;
        color: #666;
    }
    
    /* Success/Info messages */
    .stSuccess {
        background-color: #e6f7e6;
        border-radius: 8px;
    }
    
    .stInfo {
        background-color: #e6f2ff;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = PAGE_HOME

# Define page list (using constants)
# PAGES is now imported from constants

# Sidebar navigation
with st.sidebar:
    st.markdown("## 🧭 Navigation")
    page = st.radio(
        "",
        PAGES,
        index=PAGES.index(st.session_state.page),
        label_visibility="collapsed"
    )
    # Update session state when radio button changes
    st.session_state.page = page
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("VisaVerse Copilot helps you navigate global mobility with confidence.")
    
    st.markdown("---")
    st.markdown("### Resources")
    st.markdown("- [Documentation](#)")
    st.markdown("- [Support](#)")
    st.markdown("- [Contact](#)")

# Hero Section
if st.session_state.page == PAGE_HOME:
    st.markdown("""
        <div class="hero">
            <h1>✈️ VisaVerse Copilot</h1>
            <p>Your trusted assistant for global mobility, visa applications, and cross-cultural success</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🌍 Visa Assistant")
        st.markdown("Get personalized visa and work eligibility guidance based on your profile.")
        if st.button("Get Started →", key="visa"):
            st.session_state.page = PAGE_VISA
            st.rerun()
    
    with col2:
        st.markdown("### 📄 Document Checker")
        st.markdown("Verify your documents are complete and ready for submission.")
        if st.button("Check Now →", key="docs"):
            st.session_state.page = PAGE_DOCUMENTS
            st.rerun()
    
    with col3:
        st.markdown("### 🤝 Cultural Guide")
        st.markdown("Navigate cultural differences and communication styles with confidence.")
        if st.button("Learn More →", key="culture"):
            st.session_state.page = PAGE_CULTURE
            st.rerun()
    
    st.markdown("---")
    
    # Key benefits
    st.markdown("## Why VisaVerse?")
    
    benefit1, benefit2 = st.columns(2)
    
    with benefit1:
        st.markdown("### ⚡ Fast & Accurate")
        st.markdown("Get instant answers to your visa questions with AI-powered insights.")
        
        st.markdown("### 🔒 Secure & Private")
        st.markdown("Your personal information is protected and never shared.")
    
    with benefit2:
        st.markdown("### 🎯 Personalized")
        st.markdown("Tailored recommendations based on your unique situation.")
        
        st.markdown("### 🌐 Global Coverage")
        st.markdown("Support for visa applications across 150+ countries.")

# Visa & Work Eligibility Assistant
elif st.session_state.page == PAGE_VISA:
    st.markdown("# 🌍 Visa & Work Eligibility Assistant")
    st.markdown("Answer a few questions to get personalized visa recommendations.")
    
    st.markdown("---")
    
    with st.form("visa_form"):
        st.markdown("### Your Profile")
        
        col1, col2 = st.columns(2)
        
        with col1:
            current_country = st.selectbox(
                "Current Country of Residence",
                COUNTRIES
            )
            
            citizenship = st.selectbox(
                "Citizenship",
                COUNTRIES
            )
        
        with col2:
            destination = st.selectbox(
                "Destination Country",
                COUNTRIES
            )
            
            purpose = st.selectbox(
                "Purpose of Travel",
                TRAVEL_PURPOSES
            )
        
        education = st.selectbox(
            "Highest Education Level",
            EDUCATION_LEVELS
        )
        
        work_experience = st.slider("Years of Work Experience", 0, 30, 5)
        
        job_title = st.text_input("Current or Intended Job Title (optional)")
        
        submitted = st.form_submit_button("Get Visa Recommendations", use_container_width=True)
        
        if submitted:
            if current_country == "Select..." or destination == "Select..." or citizenship == "Select..." or purpose == "Select...":
                st.error("Please fill in all required fields.")
            else:
                with st.spinner("Analyzing your profile..."):
                    # Create profile for service
                    profile = {
                        'citizenship': citizenship,
                        'destination': destination,
                        'purpose': purpose,
                        'education': education,
                        'work_experience': work_experience,
                        'job_title': job_title
                    }
                    
                    # Get recommendations from service
                    recommendations = visa_service.get_visa_recommendations(profile)
                    
                    st.success("✓ Profile analyzed successfully!")
                    
                    st.markdown("---")
                    st.markdown("### 📋 Recommended Visa Options")
                    
                    if recommendations:
                        for i, rec in enumerate(recommendations, 1):
                            st.markdown(f"#### {i}. {rec['name']}")
                            st.markdown(f"""
                            - **Processing Time:** {rec['processing_time']}
                            - **Validity:** {rec['validity']}
                            - **Eligibility Score:** {rec['eligibility_score']}/100
                            - **Success Rate:** {get_success_rate_emoji(rec['success_rate'])} {rec['success_rate']}
                            """)
                            
                            with st.expander("View Requirements"):
                                st.markdown(format_requirements_list(rec['requirements']))
                    else:
                        st.info("No specific visa recommendations available for this profile. Please consult with immigration professionals.")
                    
                    # Show country-specific info
                    country_info = visa_service.get_country_info(destination)
                    if country_info:
                        st.markdown("---")
                        st.markdown(f"### 🌍 {destination} - Key Information")
                        st.markdown(f"""
                        - **Processing Authority:** {country_info.get('processing_authority', 'N/A')}
                        - **Common Visa Types:** {', '.join(country_info.get('common_visas', []))}
                        - **Special Notes:** {country_info.get('special_notes', 'N/A')}
                        """)
                    
                    st.info("💡 **Next Steps:** Review the document requirements and start preparing your application.")

# Document Readiness Checker
elif st.session_state.page == PAGE_DOCUMENTS:
    st.markdown("# 📄 Document Readiness Checker")
    st.markdown("Ensure you have all required documents before submitting your application.")
    
    st.markdown("---")
    
    visa_type = st.selectbox(
        "Select Visa Type",
        VISA_TYPES
    )
    
    if visa_type != "Select...":
        # Get requirements from service
        requirements = document_service.get_required_documents(visa_type)
        
        st.markdown("### 📋 Required Documents Checklist")
        
        # Track checked documents
        checked_docs = {}
        
        # Essential documents
        st.markdown("#### Essential Documents")
        for doc in requirements.get('essential', []):
            checked_docs[doc] = st.checkbox(doc, key=f"essential_{doc}")
        
        # Specific documents
        st.markdown(f"#### {visa_type} Visa Specific Documents")
        for doc in requirements.get('specific', []):
            checked_docs[doc] = st.checkbox(doc, key=f"specific_{doc}")
        
        st.markdown("---")
        
        if st.button("Check Readiness", use_container_width=True):
            # Calculate readiness using service
            readiness = document_service.calculate_readiness_score(visa_type, checked_docs)
            
            st.markdown("### 📊 Readiness Score")
            st.progress(readiness['percentage'] / 100)
            st.markdown(f"**{readiness['score']}%** complete ({readiness['completed']}/{readiness['total']} documents)")
            
            message = get_readiness_message(readiness['percentage'])
            
            if readiness['percentage'] == 100:
                st.success(message)
            elif readiness['percentage'] >= 70:
                st.info(message)
            else:
                st.warning(message)
            
            if readiness['missing']:
                with st.expander("Missing Documents"):
                    st.markdown(format_requirements_list(readiness['missing']))

# Cultural & Communication Guide
elif st.session_state.page == PAGE_CULTURE:
    st.markdown("# 🤝 Cultural & Communication Guide")
    st.markdown("Navigate cultural differences and communicate effectively in your destination country.")
    
    st.markdown("---")
    
    # Get available countries from service
    available_countries = culture_service.get_available_countries()
    country_options = ["Select..."] + available_countries
    
    destination_country = st.selectbox(
        "Select Your Destination Country",
        country_options
    )
    
    if destination_country != "Select...":
        st.markdown(f"### 🌏 {destination_country} - Cultural Insights")
        
        tab1, tab2, tab3, tab4 = st.tabs(["Workplace", "Communication", "Etiquette", "Tips"])
        
        # Get country data from service
        workplace = culture_service.get_workplace_culture(destination_country)
        communication = culture_service.get_communication_style(destination_country)
        etiquette = culture_service.get_business_etiquette(destination_country)
        tips = culture_service.get_cultural_tips(destination_country)
        
        with tab1:
            st.markdown("#### Workplace Culture")
            if workplace:
                st.markdown(f"""
                - **Work Style:** {workplace.get('work_style', 'N/A')}
                - **Hierarchy:** {workplace.get('hierarchy', 'N/A')}
                - **Meetings:** {workplace.get('meeting_culture', 'N/A')}
                - **Work-Life Balance:** {workplace.get('work_life_balance', 'N/A')}
                - **Decision Making:** {workplace.get('decision_making', 'N/A')}
                """)
            else:
                st.info("Workplace culture information not available for this country.")
        
        with tab2:
            st.markdown("#### Communication Style")
            if communication:
                st.markdown(f"""
                - **Directness:** {communication.get('directness', 'N/A')}
                - **Small Talk:** {communication.get('small_talk', 'N/A')}
                - **Feedback:** {communication.get('feedback', 'N/A')}
                - **Email:** {communication.get('email_tone', 'N/A')}
                - **Conflict Resolution:** {communication.get('conflict_resolution', 'N/A')}
                """)
            else:
                st.info("Communication style information not available for this country.")
        
        with tab3:
            st.markdown("#### Business Etiquette")
            if etiquette:
                st.markdown(f"""
                **Greetings:**
                {etiquette.get('greetings', 'N/A')}
                
                **Dress Code:**
                {etiquette.get('dress_code', 'N/A')}
                
                **Punctuality:**
                {etiquette.get('punctuality', 'N/A')}
                
                **Business Cards:**
                {etiquette.get('business_cards', 'N/A')}
                
                **Dining:**
                {etiquette.get('dining', 'N/A')}
                """)
            else:
                st.info("Business etiquette information not available for this country.")
        
        with tab4:
            st.markdown("#### Quick Tips")
            
            if tips:
                st.markdown("**Do's and Don'ts:**")
                for tip in tips:
                    st.markdown(f"- {tip}")
            else:
                st.info("Cultural tips not available for this country.")
            
            # Show general adaptation tips
            st.markdown("---")
            st.markdown("#### General Adaptation Tips")
            adaptation_tips = culture_service.get_cultural_adaptation_tips()
            for tip in adaptation_tips:
                st.markdown(f"✓ {tip}")
            
            st.info("💡 **Remember:** Cultural adaptation takes time. Be patient with yourself and others.")

# Footer with disclaimer
st.markdown("---")
st.markdown(f"""
    <div class="disclaimer">
        <strong>{DISCLAIMER_TEXT}</strong>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div style='text-align: center; color: #999; font-size: 0.9rem;'>{FOOTER_TEXT}</div>",
    unsafe_allow_html=True
)

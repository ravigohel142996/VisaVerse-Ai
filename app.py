"""
VisaVerse Copilot - AI-powered assistant for global mobility and visa applications
A clean, minimal Streamlit web app for visa assistance, document checking, and cultural guidance.
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="VisaVerse Copilot",
    page_icon="✈️",
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

# Sidebar navigation
with st.sidebar:
    st.markdown("## 🧭 Navigation")
    page = st.radio(
        "",
        ["Home", "Visa Assistant", "Document Checker", "Cultural Guide"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("VisaVerse Copilot helps you navigate global mobility with confidence.")
    
    st.markdown("---")
    st.markdown("### Resources")
    st.markdown("- [Documentation](#)")
    st.markdown("- [Support](#)")
    st.markdown("- [Contact](#)")

# Hero Section
if page == "Home":
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
            st.session_state.page = "Visa Assistant"
            st.rerun()
    
    with col2:
        st.markdown("### 📄 Document Checker")
        st.markdown("Verify your documents are complete and ready for submission.")
        if st.button("Check Now →", key="docs"):
            st.session_state.page = "Document Checker"
            st.rerun()
    
    with col3:
        st.markdown("### 🤝 Cultural Guide")
        st.markdown("Navigate cultural differences and communication styles with confidence.")
        if st.button("Learn More →", key="culture"):
            st.session_state.page = "Cultural Guide"
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
elif page == "Visa Assistant":
    st.markdown("# 🌍 Visa & Work Eligibility Assistant")
    st.markdown("Answer a few questions to get personalized visa recommendations.")
    
    st.markdown("---")
    
    with st.form("visa_form"):
        st.markdown("### Your Profile")
        
        col1, col2 = st.columns(2)
        
        with col1:
            current_country = st.selectbox(
                "Current Country of Residence",
                ["Select...", "United States", "United Kingdom", "Canada", "India", "Germany", "Australia", "Other"]
            )
            
            citizenship = st.selectbox(
                "Citizenship",
                ["Select...", "United States", "United Kingdom", "Canada", "India", "Germany", "Australia", "Other"]
            )
        
        with col2:
            destination = st.selectbox(
                "Destination Country",
                ["Select...", "United States", "United Kingdom", "Canada", "India", "Germany", "Australia", "Other"]
            )
            
            purpose = st.selectbox(
                "Purpose of Travel",
                ["Select...", "Work/Employment", "Study", "Business", "Tourism", "Family", "Other"]
            )
        
        education = st.selectbox(
            "Highest Education Level",
            ["Select...", "High School", "Bachelor's Degree", "Master's Degree", "PhD", "Other"]
        )
        
        work_experience = st.slider("Years of Work Experience", 0, 30, 5)
        
        job_title = st.text_input("Current or Intended Job Title (optional)")
        
        submitted = st.form_submit_button("Get Visa Recommendations", use_container_width=True)
        
        if submitted:
            if current_country == "Select..." or destination == "Select..." or citizenship == "Select...":
                st.error("Please fill in all required fields.")
            else:
                with st.spinner("Analyzing your profile..."):
                    st.success("✓ Profile analyzed successfully!")
                    
                    st.markdown("---")
                    st.markdown("### 📋 Recommended Visa Options")
                    
                    # Sample recommendations based on purpose
                    if purpose == "Work/Employment":
                        st.markdown("#### 1. Skilled Worker Visa")
                        st.markdown(f"""
                        - **Processing Time:** 3-6 weeks
                        - **Validity:** Up to 5 years
                        - **Requirements:** Job offer from licensed sponsor, meet skill level threshold
                        - **Success Rate:** High (based on your {work_experience} years of experience)
                        """)
                        
                        st.markdown("#### 2. Intra-company Transfer")
                        st.markdown("""
                        - **Processing Time:** 2-4 weeks
                        - **Validity:** Up to 5 years
                        - **Requirements:** Current employment with multinational company
                        - **Success Rate:** Very High
                        """)
                    
                    elif purpose == "Study":
                        st.markdown("#### 1. Student Visa")
                        st.markdown("""
                        - **Processing Time:** 3-4 weeks
                        - **Validity:** Duration of course + 4 months
                        - **Requirements:** Acceptance letter, proof of funds, English proficiency
                        - **Success Rate:** High
                        """)
                    
                    else:
                        st.markdown("#### 1. Standard Visitor Visa")
                        st.markdown("""
                        - **Processing Time:** 2-3 weeks
                        - **Validity:** 6 months
                        - **Requirements:** Proof of funds, return ticket, purpose of visit
                        - **Success Rate:** High
                        """)
                    
                    st.info("💡 **Next Steps:** Review the document requirements and start preparing your application.")

# Document Readiness Checker
elif page == "Document Checker":
    st.markdown("# 📄 Document Readiness Checker")
    st.markdown("Ensure you have all required documents before submitting your application.")
    
    st.markdown("---")
    
    visa_type = st.selectbox(
        "Select Visa Type",
        ["Select...", "Skilled Worker", "Student", "Tourist", "Business", "Family", "Other"]
    )
    
    if visa_type != "Select...":
        st.markdown("### 📋 Required Documents Checklist")
        
        # Common documents for all visa types
        st.markdown("#### Essential Documents")
        
        passport = st.checkbox("Valid passport (minimum 6 months validity)")
        photos = st.checkbox("Recent passport-sized photographs")
        application = st.checkbox("Completed visa application form")
        fee = st.checkbox("Visa application fee payment receipt")
        
        # Visa-specific documents
        st.markdown(f"#### {visa_type} Visa Specific Documents")
        
        if visa_type == "Skilled Worker":
            sponsor = st.checkbox("Certificate of Sponsorship from employer")
            proof_funds = st.checkbox("Proof of financial means")
            qualifications = st.checkbox("Educational certificates and transcripts")
            experience = st.checkbox("Work experience letters")
            english = st.checkbox("English language test results (IELTS/TOEFL)")
            
        elif visa_type == "Student":
            acceptance = st.checkbox("University acceptance letter")
            proof_funds_student = st.checkbox("Proof of tuition fees and living expenses")
            academic = st.checkbox("Previous academic records")
            english_student = st.checkbox("English language proficiency test")
            
        elif visa_type == "Tourist":
            itinerary = st.checkbox("Travel itinerary")
            accommodation = st.checkbox("Hotel bookings or invitation letter")
            proof_funds_tourist = st.checkbox("Bank statements (last 3 months)")
            
        elif visa_type == "Business":
            invitation = st.checkbox("Business invitation letter")
            company_docs = st.checkbox("Company registration documents")
            proof_funds_business = st.checkbox("Proof of financial stability")
        
        st.markdown("---")
        
        if st.button("Check Readiness", use_container_width=True):
            # Count checked items
            total_items = sum([passport, photos, application, fee])
            
            if visa_type == "Skilled Worker":
                total_items += sum([sponsor, proof_funds, qualifications, experience, english])
                max_items = 9
            elif visa_type == "Student":
                total_items += sum([acceptance, proof_funds_student, academic, english_student])
                max_items = 8
            elif visa_type == "Tourist":
                total_items += sum([itinerary, accommodation, proof_funds_tourist])
                max_items = 7
            elif visa_type == "Business":
                total_items += sum([invitation, company_docs, proof_funds_business])
                max_items = 7
            else:
                max_items = 4
            
            progress_pct = (total_items / max_items) * 100
            
            st.markdown("### 📊 Readiness Score")
            st.progress(progress_pct / 100)
            st.markdown(f"**{progress_pct:.0f}%** complete ({total_items}/{max_items} documents)")
            
            if progress_pct == 100:
                st.success("✓ Congratulations! You have all required documents ready.")
            elif progress_pct >= 70:
                st.info("You're almost there! Complete the remaining documents to submit your application.")
            else:
                st.warning("⚠️ You need to prepare more documents before applying.")

# Cultural & Communication Guide
elif page == "Cultural Guide":
    st.markdown("# 🤝 Cultural & Communication Guide")
    st.markdown("Navigate cultural differences and communicate effectively in your destination country.")
    
    st.markdown("---")
    
    destination_country = st.selectbox(
        "Select Your Destination Country",
        ["Select...", "United States", "United Kingdom", "Canada", "Germany", "Japan", "India", "Australia", "Other"]
    )
    
    if destination_country != "Select...":
        st.markdown(f"### 🌏 {destination_country} - Cultural Insights")
        
        tab1, tab2, tab3, tab4 = st.tabs(["Workplace", "Communication", "Etiquette", "Tips"])
        
        with tab1:
            st.markdown("#### Workplace Culture")
            
            if destination_country == "United States":
                st.markdown("""
                - **Work Style:** Direct, results-oriented, fast-paced
                - **Hierarchy:** Relatively flat, first-name basis common
                - **Meetings:** Agenda-driven, punctuality valued
                - **Work-Life Balance:** Varies by company, generally work-focused
                """)
            
            elif destination_country == "United Kingdom":
                st.markdown("""
                - **Work Style:** Professional, polite, indirect communication
                - **Hierarchy:** Moderate, respect for titles
                - **Meetings:** Structured, punctuality important
                - **Work-Life Balance:** Improving, good vacation allowance
                """)
            
            elif destination_country == "Japan":
                st.markdown("""
                - **Work Style:** Group-oriented, consensus-based, detail-focused
                - **Hierarchy:** Strict, seniority-based respect
                - **Meetings:** Formal, decisions made beforehand
                - **Work-Life Balance:** Long hours common, changing gradually
                """)
            
            else:
                st.markdown("""
                - **Work Style:** Professional environment with local customs
                - **Hierarchy:** Varies by industry and company
                - **Meetings:** Follow local business norms
                - **Work-Life Balance:** Research local expectations
                """)
        
        with tab2:
            st.markdown("#### Communication Style")
            
            if destination_country in ["United States", "Australia"]:
                st.markdown("""
                - **Directness:** Very direct, explicit communication
                - **Small Talk:** Common and encouraged
                - **Feedback:** Direct and frequent
                - **Email:** Casual but professional
                """)
            
            elif destination_country in ["United Kingdom"]:
                st.markdown("""
                - **Directness:** Indirect, polite circumlocution
                - **Small Talk:** Weather, sports, current events
                - **Feedback:** Softened with positive framing
                - **Email:** Formal and polite
                """)
            
            elif destination_country in ["Japan", "India"]:
                st.markdown("""
                - **Directness:** Indirect, context-heavy
                - **Small Talk:** Important for relationship building
                - **Feedback:** Very indirect, saving face important
                - **Email:** Formal, respectful
                """)
            
            else:
                st.markdown("""
                - **Directness:** Learn local communication norms
                - **Small Talk:** Observe and adapt
                - **Feedback:** Understand cultural context
                - **Email:** When in doubt, be formal
                """)
        
        with tab3:
            st.markdown("#### Business Etiquette")
            
            st.markdown("""
            **Greetings:**
            - Research appropriate greetings (handshake, bow, etc.)
            - Use proper titles until invited to use first names
            - Be aware of personal space preferences
            
            **Meetings:**
            - Arrive on time (or early in some cultures)
            - Dress code: business professional unless told otherwise
            - Bring business cards (essential in some cultures)
            
            **Dining:**
            - Understand table manners and customs
            - Know who pays and tipping culture
            - Be aware of dietary restrictions and preferences
            """)
        
        with tab4:
            st.markdown("#### Quick Tips")
            
            st.markdown("""
            ✓ **Do:**
            - Research and respect local customs
            - Observe before acting in unfamiliar situations
            - Ask questions when unsure
            - Show genuine interest in the culture
            - Be patient and flexible
            
            ✗ **Don't:**
            - Assume your way is the right way
            - Make cultural comparisons or criticisms
            - Rush into familiar behavior
            - Ignore local holidays and celebrations
            - Stereotype or generalize
            """)
            
            st.info("💡 **Remember:** Cultural adaptation takes time. Be patient with yourself and others.")

# Footer with disclaimer
st.markdown("---")
st.markdown("""
    <div class="disclaimer">
        <strong>⚠️ Disclaimer:</strong> VisaVerse Copilot provides general information and guidance only. 
        This is not legal advice. Visa requirements and policies change frequently. 
        Always verify information with official government sources and consult with qualified immigration professionals 
        for your specific situation.
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; color: #999; font-size: 0.9rem;'>© 2024 VisaVerse Copilot. Built for the VisaVerse AI Hackathon.</div>",
    unsafe_allow_html=True
)

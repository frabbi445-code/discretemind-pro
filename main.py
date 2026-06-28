import streamlit as st
import google.generativeai as genai
import time
import plotly.graph_objects as go
import numpy as np

# ১. পেজ সেটিংস
st.set_page_config(page_title="DiscreteMind AI Ultra Pro", page_icon="🧮", layout="centered")

# শিরোনাম ও হেডার
st.markdown("<h1 style='text-align: center; color: #38bdf8;'>🚀 DiscreteMind AI Ultra Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.2rem; font-weight: 500;'>Advanced 3D-Enhanced Discrete Mathematics Lab Solver</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.9rem;'>Presidency University | CSE Dept | AI Innovation Project</p>", unsafe_allowed_html=True)
st.write("---")

# ২. সাইডবার ডিজাইন (স্টুডেন্ট ইনফো এবং নিরাপদ API Key ইনপুট)
st.sidebar.header("🎓 Lab Project Profile")
with st.sidebar.container(border=True):
    st.write("**Developer:** MD FAZLE RABBI SOHAN")
    st.write("**Institution:** Presidency University")
    st.write("**Department:** CSE")
    st.write("**Course:** Discrete Mathematics")

st.sidebar.write("---")
st.sidebar.header("🔑 Authentication")

# ইউজার সরাসরি এখান থেকে নতুন API Key বসাবে, ফলে কোড কখনো ব্লক হবে না
user_api_key = st.sidebar.text_input(
    "তোমার Gemini API Key টি এখানে বসাও:", 
    type="password", 
    placeholder="AI Studio থেকে পাওয়া Key টি পেস্ট করো..."
)
st.sidebar.caption("💡 [Google AI Studio](https://aistudio.google.com/) থেকে ফ্রিতে ২ মিনিটে নতুন Key তৈরি করে এখানে বসাতে পারো।")

st.sidebar.write("---")
st.sidebar.header("🔗 Quick Navigation")
st.sidebar.page_link("https://presidency.edu.bd/", label="Presidency University Portal", icon="🏫")

# ৩. ৩ডি অ্যানিমেটেড মডেল সেকশন (Interactive 3D Math Topology)
st.write("### 🌐 Live 3D AI Topology Node Mesh (Lab Presentation Mode)")
st.caption("মাউস দিয়ে স্ক্রল করে ৩ডি মডেলটি জুম করো এবং ড্র্যাগ করে চারদিকে ঘুরিয়ে স্যারদের দেখাও:")

n_nodes = 40
x = np.random.standard_normal(n_nodes)
y = np.random.standard_normal(n_nodes)
z = np.random.standard_normal(n_nodes)

fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers+lines',
    marker=dict(size=6, color=z, colorscale='Viridis', opacity=0.8),
    line=dict(color='#38bdf8', width=1.5)
)])

fig.update_layout(
    margin=dict(l=0, r=0, b=0, t=0),
    scene=dict(
        xaxis=dict(showbackground=False, showticklabels=False, title=''),
        yaxis=dict(showbackground=False, showticklabels=False, title=''),
        zaxis=dict(showbackground=False, showticklabels=False, title=''),
    ),
    height=300
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ৪. ডিসক্রিট ম্যাথ টপিক সিলেকশন
topic = st.selectbox(
    "🎯 সলভ করার জন্য ডিসক্রিট ম্যাথ টপিকটি সিলেক্ট করো:", 
    [
        "📊 Truth Table & Propositional Logic (লজিক টেবিল)", 
        "⭕ Set Theory (ইউনিয়ন, ইন্টারсеকশন ও ভেন ডায়াগ্রাম)", 
        "🔢 Permutation & Combination (বিন্যাস ও সমাবেশ)"
    ]
)

# ৫. স্মার্ট প্র্যাকটিস কুইক বাটনসমূহ
st.write("💡 **স্মার্ট প্র্যাকটিস টুলস (যেকোনো একটি বাটনে ক্লিক করো):**")
col1, col2, col3 = st.columns(3)

if 'input_val' not in st.session_state:
    st.session_state.input_val = ""

if col1.button("📋 লজিক এক্সাম্পল রান"):
    st.session_state.input_val = "Prove that the logical expression (P -> Q) AND NOT Q -> NOT P is a Tautology using a truth table."
if col2.button("⭕ সেট থিওরি এক্সাম্পল রান"):
    st.session_state.input_val = "Let U = {1,2,3,4,5,6,7,8,9,10}. If A = {1,3,5,7,9} and B = {2,3,5,7}, find A U B, A n B, and A' with verification steps."
if col3.button("🔢 বিন্যাস ও সমাবেশ রান"):
    st.session_state.input_val = "In how many ways can a committee of 4 members be formed from a group of 7 men and 5 women if the committee must include exactly 2 numbers of women?"

st.write("---")

# 🔍 ইনপুট বক্স ও লাইভ মেট্রিক্স
user_query = st.text_area(
    "📝 তোমার ডিসক্রিট ম্যাথের প্রশ্নটি নিচে টাইপ করো বা এডিট করো:", 
    value=st.session_state.input_val,
    placeholder="এখানে তোমার প্রশ্নটি লেখো...", 
    height=130
)

m_col1, m_col2 = st.columns(2)
with m_col1:
    st.info(f"🔹 **ক্যারেক্টার সংখ্যা:** {len(user_query)}")
with m_col2:
    st.info(f"🔹 **মোট শব্দ সংখ্যা:** {len(user_query.split())}")

st.write("")

# অ্যাকশন বাটনসমূহ
btn_col1, btn_col2 = st.columns([4, 1])
with btn_col1:
    solve_btn = st.button("🚀 এক্সপার্ট এআই সリューション জেনারেট করো", use_container_width=True)
with btn_col2:
    if st.button("🗑️ Reset", use_container_width=True):
        st.session_state.input_val = ""
        st.rerun()

# 🧮 এআই ব্যাকএন্ড সলভিং লজিক
if solve_btn:
    if not user_api_key:
        st.error("❌ অ্যাপটি চালানোর জন্য বামপাশের সাইডবারে তোমার Gemini API Key টি বসাতে হবে!")
    elif not user_query:
        st.warning("⚠️ আগে সলভ করার জন্য কোনো প্রশ্ন ইনপুট দাও বা উপরের উদাহরণ বাটনে ক্লিক করো!")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for percent_complete in range(10, 101, 30):
            time.sleep(0.1)
            progress_bar.progress(percent_complete)
            status_text.markdown(f"⚙️ **এআই ডিপ লার্নিং লজিক প্রসেস করছে... {percent_complete}%**")
            
        with st.spinner("✨ ফাইনাল সলিউশন ফরম্যাট করা হচ্ছে..."):
            try:
                # ইউজারের দেওয়া এপিআই কি দিয়ে রান হচ্ছে
                genai.configure(api_key=user_api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"""
                You are a world-class university professor teaching Discrete Mathematics to Computer Science engineering students.
                Provide a flawless, highly structured, and academic step-by-step solution for the following problem.
                Topic Category: {topic}
                Problem: {user_query}
                
                Strict Output Structure:
                1. 📝 **Mathematical Analysis / Given Data**: Clearly define the parameters or variables given.
                2. 🛠️ **Step-by-Step Derivation**: Numbered logical steps breaking down the core formulas or laws applied.
                3. 📊 **Visual Representation/Table (if applicable)**: Render markdown tables for Truth Tables elegantly.
                4. 🎯 **Final Conclusion**: A bold final conclusion box stating the absolute definitive mathematical answer.
                """
                
                response = model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(temperature=0.15)
                )
                
                status_text.empty()
                progress_bar.empty()
                
                st.balloons()
                st.success("🎉 সমাধান সফলভাবে তৈরি হয়েছে!")
                
                with st.container(border=True):
                    st.markdown(response.text)
                
            except Exception as e:
                status_text.empty()
                progress_bar.empty()
                st.error(f"❌ রান-টাইম এরর: {e}\n\nসম্ভবত তোমার এপিআই কি-টি সঠিক নয় বা এক্সপায়ার হয়েছে। দয়া করে গুগল আই স্টুডিও থেকে নতুন কি নিয়ে চেষ্টা করো।")

st.write("---")

# 🧠 ৬. কালারফুল ইন্টারঅ্যাক্টিভ কুইজ মডিউল
st.subheader("🧠 Interactive Lab Quiz (Self-Test)")
st.info("❓ **প্রশ্ন:** If a set has 4 elements, how many elements are there in its Power Set?")

ans_col1, ans_col2, ans_col3 = st.columns(3)
if ans_col1.button("Option A: 4টি"):
    st.error("❌ ভুল উত্তর! আবার চেষ্টা করো।")
if ans_col2.button("Option B: 8টি"):
    st.error("❌ ভুল উত্তর! উপাদান সংখ্যার সূত্র হলো 2^n।")
if ans_col3.button("Option C: 16টি (Correct)"):
    st.success("🎉 চমৎকার! সঠিক উত্তর। কারণ Power Set এর উপাদান সংখ্যা হলো 2^4 = 16।")

st.write("---")
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.85rem;'>Developed by MD FAZLE RABBI SOHAN | PU CSE Innovation Lab</p>", unsafe_allow_html=True)

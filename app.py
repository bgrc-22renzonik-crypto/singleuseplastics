import streamlit as st

st.set_page_config(
    page_title="Single Use Plastics",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
}

.card {
    background-color: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}

h1, h2, p {
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 Single Use Plastics")

st.markdown("""
<div class="card">
<h2>📚 What Are Single Use Plastics?</h2>
<p>
Single-use plastics are plastic items that are used once and then thrown away.
Examples include plastic straws, shopping bags, water bottles and food packaging.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>🐢 Environmental Effects</h2>
<p>
Plastic waste can pollute oceans, rivers and land. Animals can mistake plastic
for food, which may harm them. Plastic can also break into tiny pieces called
microplastics.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>♻️ How Can We Help?</h2>
<p>
Use reusable bags, reusable bottles and recycle correctly. Small actions can
make a big difference.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>💡 Conclusion</h2>
<p>
Single-use plastics are a major environmental problem, but everyone can help by
making better choices every day.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.write("Created for Year 7–8 Students 🌎")

# import streamlit as st

# st.set_page_config(page_title="Streamlit Text Elements Showcase", layout="centered")

# st.title("Streamlit Text Elements Showcase")
# tabs = st.tabs([
#     "Basics",
#     "Markdown",
#     "Badges",
# ])

# with tabs[0]:
#     with st.echo():
#         st.title("This is `st.title()` (largest)",anchor='big_title')
#         st.header("This is `st.header()` (medium)",\
#                 help='tips of my project',\
#                 divider='red')
#         st.subheader("This is `st.subheader()` (small)")
#         st.caption("This is a small, muted caption (good for footnotes).")
#         st.divider()


# with tabs[1]:
#     st.header("Markdown")
#     md = """
# # H1 Heading (Markdown)
# ## H2 Heading
# ### H3 Heading

# **Bold**, *italic*, ~~strikethrough~~, and `inline code`.

# - Bullet list item 1
# - Bullet list item 2
#   - Nested item

# 1. Ordered item A
# 2. Ordered item B

# > Blockquote: Markdown is great for rich formatting.

# **Table**  
# | Name | Type | Notes |
# |------|------|-------|
# | `st.markdown` | function | Renders Markdown |
# | `st.write` | function | Renders many types |


# Horizontal rule (Markdown):  
# ---
# """
#     st.markdown(md)
#     with st.expander("Show Markdown source"):
#         st.code(md, language="markdown")

# with tabs[2]:
#     with st.echo():
#         st.header("Badges")
#         st.caption("Badges quickly spotlight key status or type information (e.g., NEW, Video), enabling fast scanning and comprehension without reading detailed text.")
#         st.badge("COMP4415/ 5415")
#         st.badge("Multimedia",color='orange')
#         st.badge("Streamlit", icon=":material/check:", color="green")


import streamlit as st

# 页面配置
st.set_page_config(
    page_title="Magic Fruit Company",
    layout="centered",
    page_icon="🍎"
)

# 标题和口号
st.title("🍎 Magic Fruit")
st.subheader("Farm Direct · Daily Fresh")
st.caption("From our orchards to your table, every fruit is a story of freshness and trust.")

st.divider()

# 公司简介
st.header("About Us")
st.write("""
Magic Fruit is a fresh fruit e-commerce platform that connects consumers directly 
with trusted local farms. Our mission is to make healthy living easier by delivering 
fresh, nutritious fruits from orchards to homes with full transparency and quality assurance.
""")

# 核心价值
st.header("Our Values")
col1, col2, col3 = st.columns(3)
with col1:
    st.badge("Freshness", color="green")
    st.write("Picked at the right time to guarantee natural taste and nutrition.")
with col2:
    st.badge("Transparency", color="orange")
    st.write("We show the complete journey of fruits, from farm to store.")
with col3:
    st.badge("Trust", color="blue")
    st.write("Strict quality checks ensure only the best fruits reach you.")

st.divider()

# 产品展示（示例）
st.header("Our Products")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("assets/myfile/startpage/apple.png", caption="Red Apples")
with col2:
    st.image("assets/myfile/startpage/organ.png", caption="Fresh Oranges")
with col3:
    st.image("assets/myfile/startpage/Grapes.png", caption="Sweet Grapes")

st.divider()

# 供应链故事
st.header("Farm-to-Store Journey")
st.write("""
Every fruit has a story. From harvesting in the orchard, quality inspection, sorting, 
and packaging, to transportation and market sales, we ensure transparency 
and freshness at every step.
""")
st.video("https://www.youtube.com/watch?v=8gJ5i3h2j0U")  # 这里可以替换为你后续做的动画视频链接

st.divider()

# 联系方式
st.header("Contact Us")
st.write("""
📍 Address: 123 Orchard Road, Sydney  
📧 Email: contact@magicfruit.com  
📞 Phone: +61 400 123 456
""")
st.caption("Follow us on social media for more updates 🍇 🍊 🍌")

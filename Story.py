
# pages/Poster.py
# import streamlit as st
# import time

# st.set_page_config(page_title="Poster · Multimedia Container", page_icon="🖼️", layout="wide")
# st.title('Storyboard')
# st.code('''
# row1 = st.columns(3)
# row2 = st.columns(3)
# for col in row1 + row2:
#     tile = col.container(border=True)
#     tile.image("assets/image_icon.png")
#     tile.divider()
#     tile.text("Lorem ipsum is placeholder text commonly used in the graphic," \
#             "  print, and publishing industries for previewing layouts and visual mockups.")
#     tile.divider()
# ''',wrap_lines=True)

# row1 = st.columns(3)
# row2 = st.columns(3)

# for col in row1 + row2:
#     tile = col.container(border=True)
#     tile.image("assets/image_icon.png")
#     tile.divider()
#     tile.text("Lorem ipsum is placeholder text commonly used in the graphic," \
#             "  print, and publishing industries for previewing layouts and visual mockups.")
#     tile.divider()
    

import streamlit as st

st.set_page_config(page_title="Poster · Multimedia Container", page_icon="🖼️", layout="wide")
st.title('Storyboard')

# 1) 把 6 张图与描述放到一个列表里（按你想显示的顺序）
items = [
    {"img": "assets/myfile/storyboard/1.png", "text": "On the farm, a farmer is inspecting and picking ripe oranges, ensuring they are fresh and high-quality. The green truck is ready for transport."},
    {"img": "assets/myfile/storyboard/2.png", "text": "In the factory, a worker is checking the oranges on the conveyor belt, removing any that do not meet quality standards."},
    {"img": "assets/myfile/storyboard/3.png", "text": "The sorted fruits are placed in blue crates and neatly stored on shelves, waiting for packaging and delivery."},
    {"img": "assets/myfile/storyboard/4.png", "text": "A worker uses a forklift to load the packaged fruit boxes onto the green delivery truck, preparing them for shipment."},
    {"img": "assets/myfile/storyboard/5.png", "text": "The green delivery truck travels on the road, bringing the fresh fruits quickly to the city markets and stores."},
    {"img": "assets/myfile/storyboard/6.png", "text": "At the farmers' market, a customer buys fresh oranges and vegetables, completing the farm-to-table journey."},
]

# 2) 先创建两行三列
rows = [st.columns(3), st.columns(3)]

# 3) 循环渲染：第 i 个元素放到第 i//3 行、第 i%3 列
for i, item in enumerate(items):
    col = rows[i // 3][i % 3]
    with col.container(border=True):
        # 如果图片大小不一，建议用 use_column_width=True 自适应列宽
        st.image(item["img"], use_container_width=True)
        st.divider()
        st.write(item["text"])
        st.divider()

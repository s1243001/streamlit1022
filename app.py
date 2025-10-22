import streamlit as st
# 1.使用 st.Page() 定義所有頁面
# 注意st.Page() 會自動尋找 .py 檔案
# Emoji 列表 https://tw.piliapp.com/emoji/list/
pages = [
 st.Page("page_home.py", title="專案首頁", icon="🏠"),
 st.Page("page_map.py", title="互動地圖瀏覽器", icon="🗺️"),
 st.Page("page_about.py", title="關於我們", icon="🙋‍♀️")
]
# 2. 使用 st.navigation() 建立導覽 (例如在側邊攔)
with st.sidebar:
 st.title("App 導覽")
 # st.navigation() 會回傳被選的頁面
 selected_page = st.navigation(pages)
# 3. 執行被選的頁面
selected_page.run()
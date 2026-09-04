import streamlit as st
import os

# Cấu hình trang
st.set_page_config(
    page_title="CV - Nguyễn Ngọc Lê Na",
    page_icon="📄",
    layout="wide"
)

# CSS tùy chỉnh giao diện CV
st.markdown("""
    <style>
    .main {
        background-color: #fcfbfa;
    }
    .main-title {
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #7f8c8d;
        font-size: 20px;
        margin-bottom: 20px;
    }
    .section-header {
        color: #8c6d58;
        border-bottom: 2px solid #8c6d58;
        padding-bottom: 5px;
        margin-top: 15px;
        margin-bottom: 15px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Chia cột chính (Cột trái: Ảnh & Thông tin cá nhân | Cột phải: Nội dung chính)
col_left, col_right = st.columns([1, 2], gap="large")

# ================= CỘT TRÁI =================
with col_left:
    # HIỂN THỊ ẢNH ĐẠI DIỆN TỪ FILE TRONG MÁY
    # Lưu ý: Hãy đổi tên file ảnh của bạn thành 'avatar.jpg' (hoặc 'avatar.png') 
    # và để cùng thư mục với file code app.py này.
    image_path = "avatar.jpg" 
    
    if os.path.exists(image_path):
        st.image(image_path, width=200)
    elif os.path.exists("avatar.png"):
        st.image("avatar.png", width=200)
    else:
        st.info("⚠️ Vui lòng đặt file ảnh đại diện ('avatar.jpg' hoặc 'avatar.png') cùng thư mục với file app.py")

    st.markdown('<p class="section-header">LIÊN HỆ</p>', unsafe_allow_html=True)[cite: 1]
    st.write("📞 0376524871")
    st.write("✉️ nle9960@gmail.com")
    st.write("📅 12-02-2005")
    st.write("📍 An Phú Đông, TP. Hồ Chí Minh")
    
    st.markdown('<p class="section-header">HỌC VẤN</p>', unsafe_allow_html=True)
    st.markdown("**ĐẠI HỌC NGUYỄN TẤT THÀNH**")
    st.write("2023 - 2026")
    st.write("• Chuyên ngành: Tài chính - Ngân hàng")
    st.write("• GPA: 3.82/4.00")
    
    st.markdown('<p class="section-header">NGÔN NGỮ</p>', unsafe_allow_html=True)
    st.write("• Tiếng Anh")
    st.write("• Tiếng Việt")
    
    st.markdown('<p class="section-header">SỞ THÍCH</p>', unsafe_allow_html=True)
    st.write("• Nghe nhạc")
    st.write("• Nấu ăn")
    st.write("• Đọc sách")

# ================= CỘT PHẢI =================
with col_right:
    st.markdown('<h1 class="main-title">NGUYỄN NGỌC LÊ NA</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Thực tập sinh</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="section-header">MỤC TIÊU NGHỀ NGHIỆP</p>', unsafe_allow_html=True)
    st.write("""
    Tìm kiếm cơ hội thực tập tại ngân hàng nhằm học hỏi kinh nghiệm thực tế trong lĩnh vực tài chính - ngân hàng và hiểu rõ hơn về các hoạt động nghiệp vụ trong môi trường làm việc chuyên nghiệp.
    
    Mong muốn được phát triển các kỹ năng chuyên môn, kỹ năng phân tích và giao tiếp, từ đó tích lũy kinh nghiệm để định hướng phát triển nghề nghiệp lâu dài trong ngành tài chính - ngân hàng.
    """)
    
    st.markdown('<p class="section-header">HOẠT ĐỘNG NGOẠI KHÓA</p>', unsafe_allow_html=True)
    st.markdown("""
    • Cộng tác viên hỗ trợ tuyển sinh 2024.  
    • Workshop Khởi đầu thông minh - Chiến lược đầu tư chứng khoán 2024.  
    • Chiến dịch tình nguyện mùa hè xanh 2025.  
    • Hoạt động Trải nghiệm chương trình HUB FORUM 2025.  
    • Lễ hội trung thu nghĩa tình 2025.  
    • Tham gia cuộc thi đầu tư chứng khoán trên ứng dụng Chứng khoán Rồng Việt 2025.
    """)
    
    st.markdown('<p class="section-header">KỸ NĂNG</p>', unsafe_allow_html=True)
    st.markdown("""
    • Kỹ năng giao tiếp, lắng nghe và thuyết phục  
    • Kỹ năng làm việc nhóm  
    • Kỹ năng giải quyết vấn đề và quản lý thời gian  
    • Kỹ năng hành chính văn phòng  
    • Kỹ năng tin học văn phòng cơ bản  
    • Kỹ năng ngoại ngữ
    """)
    
    st.markdown('<p class="section-header">THÀNH TÍCH</p>', unsafe_allow_html=True)
    st.markdown("""
    • Học bổng khuyến khích học tập của Vietcombank 2024.  
    • Học bổng khuyến khích học tập của Trường Đại học Nguyễn Tất Thành (2024 - 2025).  
    • Đạt thành tích học tập loại Xuất sắc năm (2024 - 2025).
    """)

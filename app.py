import streamlit as st
import os

# 1. Cấu hình trang Streamlit
st.set_page_config(
    page_title="CV - Nguyễn Ngọc Lê Na",
    page_icon="📄",
    layout="wide"
)

# 2. Định nghĩa CSS tùy chỉnh để làm đẹp giao diện CV
custom_css = """
<style>
    /* Nền chung */
    .stApp {
        background-color: #faf8f5;
    }
    
    /* Tiêu đề chính */
    .name-title {
        color: #2c3e50;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 0px;
        letter-spacing: 1px;
    }
    
    .job-title {
        color: #7f8c8d;
        font-size: 20px;
        font-weight: 500;
        margin-top: 5px;
        margin-bottom: 25px;
    }
    
    /* Cột bên trái */
    .left-section-title {
        color: #7d5a44;
        font-size: 18px;
        font-weight: bold;
        border-bottom: 2px solid #7d5a44;
        padding-bottom: 5px;
        margin-top: 20px;
        margin-bottom: 12px;
        text-transform: uppercase;
    }
    
    /* Cột bên phải */
    .right-section-title {
        color: #7d5a44;
        font-size: 18px;
        font-weight: bold;
        border-bottom: 2px solid #7d5a44;
        padding-bottom: 5px;
        margin-top: 20px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }
    
    /* Nội dung văn bản */
    .info-text {
        font-size: 15px;
        color: #333333;
        line-height: 1.6;
    }
    
    ul {
        padding-left: 20px;
    }
    
    li {
        margin-bottom: 6px;
        font-size: 15px;
        color: #333333;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Chia bố cục làm 2 cột (Cột trái: 30%, Cột phải: 70%)
col1, col2 = st.columns([1, 2], gap="large")

# ==================== CỘT TRÁI ====================
with col1:
    # Hiển thị ảnh đại diện
    image_files = ["avatar.jpg", "avatar.png", "avatar.jpeg"]
    found_image = False
    
    for img_file in image_files:
        if os.path.exists(img_file):
            st.image(img_file, width=200)
            found_image = True
            break
            
    if not found_image:
        # Khung hình ảnh tạm nếu chưa bỏ file ảnh vào
        st.warning("⚠️ Chưa tìm thấy file 'avatar.jpg'. Bạn nhớ copy file ảnh vào cùng thư mục nhé!")

    # THÔNG TIN LIÊN HỆ
    st.markdown('<div class="left-section-title">LIÊN HỆ</div>', unsafe_allow_html=True)[cite: 1]
    st.markdown("""
    <div class="info-text">
    📞 0376524871<br>
    ✉️ nle9960@gmail.com<br>
    📅 12-02-2005<br>
    📍 An Phú Đông, TP. Hồ Chí Minh
    </div>
    """, unsafe_allow_html=True)

    # HỌC VẤN
    st.markdown('<div class="left-section-title">HỌC VẤN</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-text">
    <b>ĐẠI HỌC NGUYỄN TẤT THÀNH</b><br>
    2023 - 2026<br>
    Chuyên ngành: Tài chính - Ngân hàng<br>
    GPA: 3.82/4.00
    </div>
    """, unsafe_allow_html=True)

    # NGÔN NGỮ
    st.markdown('<div class="left-section-title">NGÔN NGỮ</div>', unsafe_allow_html=True)
    st.markdown("""
    * Tiếng Anh
    * Tiếng Việt
    """)

    # SỞ THÍCH
    st.markdown('<div class="left-section-title">SỞ THÍCH</div>', unsafe_allow_html=True)
    st.markdown("""
    * Nghe nhạc
    * Nấu ăn
    * Đọc sách
    """)

# ==================== CỘT PHẢI ====================
with col2:
    # Họ tên và Chức danh
    st.markdown('<div class="name-title">NGUYỄN NGỌC LÊ NA</div>', unsafe_allow_html=True)
    st.markdown('<div class="job-title">Thực tập sinh</div>', unsafe_allow_html=True)

    # MỤC TIÊU NGHỀ NGHIỆP
    st.markdown('<div class="right-section-title">MỤC TIÊU NGHỀ NGHIỆP</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-text">
    Tìm kiếm cơ hội thực tập tại ngân hàng nhằm học hỏi kinh nghiệm thực tế trong lĩnh vực tài chính - ngân hàng và hiểu rõ hơn về các hoạt động nghiệp vụ trong môi trường làm việc chuyên nghiệp. <br><br>
    Mong muốn được phát triển các kỹ năng chuyên môn, kỹ năng phân tích và giao tiếp, từ đó tích lũy kinh nghiệm để định hướng phát triển nghề nghiệp lâu dài trong ngành tài chính - ngân hàng.
    </div>
    """, unsafe_allow_html=True)

    # HOẠT ĐỘNG NGOẠI KHÓA
    st.markdown('<div class="right-section-title">HOẠT ĐỘNG NGOẠI KHÓA</div>', unsafe_allow_html=True)
    st.markdown("""
    * Cộng tác viên hỗ trợ tuyển sinh 2024.
    * Workshop Khởi đầu thông minh - Chiến lược đầu tư chứng khoán 2024.
    * Chiến dịch tình nguyện mùa hè xanh 2025.
    * Hoạt động Trải nghiệm chương trình HUB FORUM 2025.
    * Lễ hội trung thu nghĩa tình 2025.
    * Tham gia cuộc thi đầu tư chứng khoán trên ứng dụng Chứng khoán Rồng Việt 2025.
    """)

    # KỸ NĂNG
    st.markdown('<div class="right-section-title">KỸ NĂNG</div>', unsafe_allow_html=True)
    st.markdown("""
    * Kỹ năng giao tiếp, lắng nghe và thuyết phục
    * Kỹ năng làm việc nhóm
    * Kỹ năng giải quyết vấn đề và quản lý thời gian
    * Kỹ năng hành chính văn phòng
    * Kỹ năng tin học văn phòng cơ bản
    * Kỹ năng ngoại ngữ
    """)

    # THÀNH TÍCH
    st.markdown('<div class="right-section-title">THÀNH TÍCH</div>', unsafe_allow_html=True)
    st.markdown("""
    * Học bổng khuyến khích học tập của Vietcombank 2024.
    * Học bổng khuyến khích học tập của Trường Đại học Nguyễn Tất Thành (2024 - 2025).
    * Đạt thành tích học tập loại Xuất sắc năm (2024 - 2025).
    """)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    "Họ và tên": [
        "Nguyễn Thị Hoài An",
        "Trần Văn Bảo",
        "Phan Thanh Hùng",
        "Lê Châu Phong",
        "Trần Thanh Nam",
        "Võ Thị Anh Thi",
        "Võ Thị Anh Thư",
        "Bùi Thị Diễm Nhung",
        "Nguyễn Thị Yến Vy",
        "Trần Phùng Tấn Quân"
    ],
    "Điểm chuyên cần": [9, 10, 8, 7, 9, 6, 10, 8, 7, 10],
    "Điểm giữa kỳ": [8, 7.7, 9, 6.5, 8.5, 7, 9.5, 8, 7.5, 9],
    "Điểm cuối kỳ": [8.5, 8, 9.5, 7, 9, 8, 9, 8.5, 8, 9.5]
}

df = pd.DataFrame(data)

df["Tong_ket"] = (
    0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

st.subheader("Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

st.subheader("Thống kê")

st.write("Điểm trung bình của lớp:", round(df["Tong_ket"].mean(), 3))

st.write("Sinh viên điểm cao nhất:")
st.write(df.loc[df["Tong_ket"].idxmax()])

st.write("Sinh viên điểm thấp nhất:")
st.write(df.loc[df["Tong_ket"].idxmin()])

st.write("Số sinh viên đạt:", int((df["Tong_ket"] >= 5).sum()))

st.subheader("Tra cứu sinh viên")

ten = st.selectbox("Chọn sinh viên", df["Họ và tên"])
sv = df[df["Họ và tên"] == ten].iloc[0]

st.write("Điểm chuyên cần:", sv["Điểm chuyên cần"])
st.write("Điểm giữa kỳ:", sv["Điểm giữa kỳ"])
st.write("Điểm cuối kỳ:", sv["Điểm cuối kỳ"])
st.write("Điểm tổng kết:", round(sv["Tong_ket"], 2))
st.write("Xếp loại:", sv["Xep_loai"])

st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df["Họ và tên"], df["Tong_ket"], color="skyblue")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ và tên")
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlim(0, 10)
plt.tight_layout()

st.pyplot(fig)

st.caption("Người tạo ứng dụng: THÔNG THỊ ĐAN ĐAN - MSSV: 060307008918")
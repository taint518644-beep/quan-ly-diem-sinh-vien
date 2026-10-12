import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

# Du lieu sinh vien
data = {
    "Ho_ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Van Cuong",
        "Pham Thi Dung",
        "Hoang Van Em",
        "Vo Thi Giang",
        "Dang Van Huy",
        "Bui Thi Lan",
        "Do Van Minh",
        "Ngo Thi Nga"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 9, 7, 5, 10],
    "Giua_ky":    [8, 7, 6, 9, 5, 8, 7, 6, 4, 9],
    "Cuoi_ky":    [9, 8, 7, 9, 6, 7, 8, 5, 4, 10]
}

df = pd.DataFrame(data)

# Tinh diem tong ket
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
).round(2)

# Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Tieu de trang web
st.title("QUAN LY DIEM SINH VIEN")
st.write("Bang diem va ket qua hoc tap cua 10 sinh vien.")

# Hien thi bang diem
st.subheader("1. Bang diem sinh vien")

bang_diem = df.rename(columns={
    "Ho_ten": "Ho va ten",
    "Chuyen_can": "Chuyen can",
    "Giua_ky": "Giua ky",
    "Cuoi_ky": "Cuoi ky",
    "Tong_ket": "Tong ket",
    "Xep_loai": "Xep loai"
})

st.dataframe(bang_diem, use_container_width=True)

# Thong ke
st.subheader("2. Thong ke ket qua")

diem_tb = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

col1, col2, col3, col4 = st.columns(4)

col1.metric("Diem trung binh", f"{diem_tb:.2f}")
col2.metric("So sinh vien dat", f"{so_sv_dat}/10")
col3.metric("Diem cao nhat", f"{sv_max['Tong_ket']:.2f}")
col4.metric("Diem thap nhat", f"{sv_min['Tong_ket']:.2f}")

st.write(
    "Sinh vien cao nhat:",
    sv_max["Ho_ten"],
    "-",
    sv_max["Tong_ket"]
)

st.write(
    "Sinh vien thap nhat:",
    sv_min["Ho_ten"],
    "-",
    sv_min["Tong_ket"]
)

# Chon sinh vien bang Selectbox
st.subheader("3. Tra cuu diem theo sinh vien")

ten_sv = st.selectbox(
    "Chon mot sinh vien:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write("Ho va ten:", sv["Ho_ten"])
st.write("Diem chuyen can:", sv["Chuyen_can"])
st.write("Diem giua ky:", sv["Giua_ky"])
st.write("Diem cuoi ky:", sv["Cuoi_ky"])
st.write("Diem tong ket:", f"{sv['Tong_ket']:.2f}")
st.write("Xep loai:", sv["Xep_loai"])

# Bieu do cot
st.subheader("4. Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])

ax.set_title("DIEM TONG KET CUA 10 SINH VIEN")
ax.set_xlabel("Ho va ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# Thong tin nguoi tao
st.divider()
st.caption("Nguoi tao: [Nguyen Tan Tai] - MSSV: [051208008644]")

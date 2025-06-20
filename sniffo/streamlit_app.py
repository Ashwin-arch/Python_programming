import streamlit as st
from crypto import caesar
from packets.scanner import scan_ports  # Make sure this file exists

st.set_page_config(page_title="Sniffo", layout="wide")
st.title("🛡️ Sniffo - Cryptography & Network Security Toolkit")
st.markdown("---")

# Sidebar
section = st.sidebar.radio("Choose Section", [
    "Home", 
    "Caesar Cipher", 
    "Network Scan"
])

# Home Section
if section == "Home":
    st.subheader("🔐 Welcome to Sniffo")
    st.write("Use the sidebar to test cryptographic tools and view network info.")

# Caesar Cipher Section
elif section == "Caesar Cipher":
    st.subheader("🔑 Caesar Cipher Tool")
    text = st.text_input("Enter text")
    shift = st.slider("Shift", 1, 25, 3)

    if st.button("Encrypt"):
        if text:
            encrypted = caesar.encrypt(text, shift)
            st.success(f"Encrypted Text: `{encrypted}`")
        else:
            st.warning("Please enter text to encrypt.")

    if st.button("Decrypt"):
        if text:
            decrypted = caesar.decrypt(text, shift)
            st.success(f"Decrypted Text: `{decrypted}`")
        else:
            st.warning("Please enter text to decrypt.")

# Network Scan Section
elif section == "Network Scan":
    st.subheader("🌐 Port Scanner")
    target_ip = st.text_input("Enter IP to scan", value="127.0.0.1")
    common_ports = [21, 22, 23, 25, 53, 80, 443, 8080]

    if st.button("Scan"):
        with st.spinner("Scanning..."):
            result = scan_ports(target_ip, common_ports)

        if result:
            st.success(f"Open ports on {target_ip}: {result}")
            st.dataframe({"Open Ports": result})
        else:
            st.info(f"No common ports open on {target_ip}.")

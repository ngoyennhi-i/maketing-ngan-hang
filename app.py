)


# ==========================================
# TRANG ADMIN
# ==========================================

elif page == "🔐 Admin":

    st.title("🔐 ADMIN")

    st.divider()


    # ======================================
    # ĐĂNG NHẬP
    # ======================================

    if "admin_logged_in" not in st.session_state:

        st.session_state.admin_logged_in = False


    if not st.session_state.admin_logged_in:

        password = st.text_input(
            "🔑 Mật khẩu",
            type="password"
        )


        if st.button(
            "ĐĂNG NHẬP",
            type="primary"
        ):

            if password == "123456":

                st.session_state.admin_logged_in = True

                st.rerun()

            else:

                st.error(
                    "❌ Sai mật khẩu."
                )


    # ======================================
    # ADMIN ĐÃ ĐĂNG NHẬP
    # ======================================

    else:

        col1, col2 = st.columns(
            [5, 1]
        )


        with col1:

            st.subheader(
                "📊 DANH SÁCH KHÁCH HÀNG"
            )


        with col2:

            if st.button("🚪 Đăng xuất"):

                st.session_state.admin_logged_in = False

                st.rerun()


        st.divider()


        # ==================================
        # KIỂM TRA DỮ LIỆU
        # ==================================

        if len(st.session_state.customers) == 0:

            st.info(
                "📭 Chưa có khách hàng."
            )


        else:

            # ==============================
            # CHUYỂN SANG DATAFRAME
            # ==============================

            df = pd.DataFrame(
                st.session_state.customers
            )


            # ==============================
            # TỔNG KHÁCH HÀNG
            # ==============================

            st.metric(
                "👥 Tổng số khách hàng",
                len(df)
            )


            st.divider()


            # ==============================
            # HIỂN THỊ DANH SÁCH
            # ==============================

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )


            st.divider()


            # ==============================
            # XUẤT EXCEL
            # ==============================

            excel_file = export_excel()


            st.download_button(
                label="📥 XUẤT FILE EXCEL",
                data=excel_file,
                file_name="danh_sach_khach_hang.xlsx",
                mime=(
                    "application/vnd.openxmlformats-officedocument."
                    "spreadsheetml.sheet"
                ),
                use_container_width=True
            )

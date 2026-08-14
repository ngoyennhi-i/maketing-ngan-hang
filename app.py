st.subheader("🔑 Đăng nhập Admin")

        password = st.text_input(
            "Mật khẩu",
            type="password"
        )

        if st.button(
            "Đăng nhập",
            type="primary"
        ):

            if password == "123456":

                st.session_state.admin_logged_in = True

                st.success("✅ Đăng nhập thành công!")

                st.rerun()

            else:

                st.error("❌ Sai mật khẩu.")

    else:

        # =========================
        # HEADER ADMIN
        # =========================

        col1, col2 = st.columns([5, 1])

        with col1:

            st.subheader("📊 Danh sách khách hàng")

        with col2:

            if st.button("🚪 Đăng xuất"):

                st.session_state.admin_logged_in = False

                st.rerun()

        # =========================
        # LẤY DỮ LIỆU
        # =========================

        df = get_customers()

        if df.empty:

            st.info(
                "📭 Chưa có thông tin khách hàng."
            )

        else:

            # =========================
            # THỐNG KÊ
            # =========================

            st.metric(
                "👥 Tổng số khách hàng",
                len(df)
            )

            st.divider()

            # =========================
            # HIỂN THỊ BẢNG
            # =========================

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.divider()

            # =========================
            # XUẤT EXCEL
            # =========================

            excel_file = export_excel(df)

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

            st.divider()

            # =========================
            # XÓA KHÁCH HÀNG
            # =========================

            st.subheader("🗑️ Xóa khách hàng")

            customer_id = st.number_input(
                "Nhập STT khách hàng cần xóa",
                min_value=1,
                step=1
            )

            if st.button(
                "🗑️ XÓA KHÁCH HÀNG",
                type="secondary"
            ):

                delete_customer(customer_id)

                st.success(
                    "✅ Đã xóa khách hàng."
                )

                st.rerun()

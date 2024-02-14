from django.contrib.admin import AdminSite


class WebLoggerAdminSite(AdminSite):
    title_header = "Web Logger admin"
    site_header = "Web Logger admin"
    site_title = "Web Logger admin"
    index_title = "Web Logger admin"


admin_site = WebLoggerAdminSite(name="web_logger_admin")

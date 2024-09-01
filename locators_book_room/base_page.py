class BasePage:
    def __init__(self, page):
        self.page = page

    def get_by_text(self, text):
        return self.page.get_by_text(text)

    def get_by_label(self, label):
        return self.page.get_by_label(label)

    def get_by_placeholder(self, placeholder):
        return self.page.get_by_placeholder(placeholder)

    def get_by_id(self, id):
        return self.page.get_by_id(id)

    def get_by_alt_text(self, alt_text):
        return self.page.get_by_alt_text(alt_text)

    def get_by_title(self, title):
        return self.page.get_by_title(title)

    def get_by_role(self, role):
        return self.page.get_by_role(role)



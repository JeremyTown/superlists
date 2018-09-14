from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string


# class SmokeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)

class HomePageTest(TestCase):
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    # def test_home_page_return_correct_html(self):
        # 利用 Django 提供的 render_to_string 函数
        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode('utf-8')
        # expected_html = render_to_string('home.html')
        # self.assertEqual(html, expected_html)

        # 调用 self.client.get，并传入要测试的 URL
        # response = self.client.get('/')
        # html = response.content.decode('utf-8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))
        # self.assertTemplateUsed(response, 'home.html')
        # self.assertTemplateUsed(response, 'wrong.html')
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
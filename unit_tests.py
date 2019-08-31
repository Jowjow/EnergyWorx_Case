import unittest, server, data_transfer


class BackendTest(unittest.TestCase):


    def test_success_validate(self):
        valid_code = 'awk_11'
        self.assertEqual(True, server.validate(valid_code))

    def test_fail_validate1(self):
        valid_code = 'awk_$#'
        self.assertEqual(False, server.validate(valid_code))

    def test_fail_validate2(self):
        valid_code = 'awk_99999'
        self.assertEqual(False, server.validate(valid_code))

    def test_fail_validate3(self):
        valid_code = 'awk'
        self.assertEqual(False, server.validate(valid_code))

    def test_generate(self):
        code = server.generate_shortcode()
        self.assertTrue(server.validate(code))

    def test_success_code_exists(self):
        self.assertTrue(server.shortcode_exists("ewx123"))

    def test_fail_code_exists(self): #test_data_transfer_get
        self.assertFalse(server.shortcode_exists("ewx1234"))

    def test_create_url_and_update(self):
        shortcode = 'tsttst'
        data_transfer.create_url('https://wwww.test.com', 'tsttst')
        self.assertTrue(server.shortcode_exists('tsttst'))
        data = data_transfer.get_shortcode(shortcode)
        redirect_count = data['data'][0]['RedirectCount']
        last_redirect = data['data'][0]['LastRedirect']
        data_transfer.update_shortcode(shortcode)
        data2 = data_transfer.get_shortcode(shortcode)
        redirect_count2 = data2['data'][0]['RedirectCount']
        last_redirect2 = data2['data'][0]['LastRedirect']
        self.assertGreater(redirect_count2, redirect_count)
        self.assertGreater(last_redirect2, last_redirect)


    def test_delete_created_entry(self):
        data_transfer.delete_shortcode_for_test('tsttst')

if __name__ == '__main__':
    unittest.main()
import unittest
import main


class TestBankingSystem(unittest.TestCase):

    # Test account creation
    def test_create_account(self):
        main.create_account()
        self.assertEqual(main.output, "Account successfully added.")

    # Test account deletion
    def test_delete_account(self):
        main.delete_account()
        self.assertEqual(main.output, "Account successfully deleted.")

    # Test editing account name
    def test_edit_account(self):
        main.edit_account()
        self.assertEqual(main.output, "Account name updated.")

    # Test deposit
    def test_deposit(self):
        main.manage_transaction()
        self.assertEqual(main.output, "Money added successfully.")

    # Test withdraw
    def test_withdraw(self):
        main.manage_transaction()
        self.assertEqual(main.output, "Money was taken out successfully.")

    # Test balance check
    def test_check_balance(self):
        main.manage_transaction()
        self.assertTrue("Balance:" in main.output)


if __name__ == '__main__':
    unittest.main()

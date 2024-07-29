#!/usr/bin/env python3
"""
declare the TestGithubOrgClient(unittest.TestCase)
class and implement the test_org method.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json', return_value={"login": "google"})
    def test_org(self, org_name, expected_result, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
                    f"https://api.github.com/orgs/{org_name}"
                    )
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

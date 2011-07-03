"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from django.utils.unittest import TestCase
#from django.test import TestCase
from mathnews.prodsys.models import Issue
import datetime;

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class IssueTest(TestCase):
    def test_create_issue_nocover(self):
        """
        Tests that an article can be created with no cover.
        """
        i = Issue(slug='test',volume=0,issue=0,pub_date=datetime.datetime.now(),cover_image=None,cover_caption="");
        i.full_clean()
        i.save()

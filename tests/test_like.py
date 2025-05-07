
"""
test_like.py

Automated test suite using pytest to test Twitter like functionality via API.
Tests include:
- Liking a valid tweet (already liked is acceptable)
- Handling an invalid tweet ID
"""

import sys
import os
import pytest

# Add root directory to path so pytest can find like_tweet.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from like_tweet import like_tweet

def test_invalid_tweet_id():
    result = like_tweet("123")  # Invalid tweet ID
    assert result != True, "Should not succeed with invalid tweet ID"

def test_like_valid_tweet():
    tweet_id = "1912946113662910812"  # Your tweet URL ID
    result = like_tweet(tweet_id)
    assert result is True or result == 403, f"Expected success or already liked, got {result}"

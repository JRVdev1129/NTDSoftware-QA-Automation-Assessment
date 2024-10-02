Feature: Google Search Functionality
  As a user, User wants to search on Google and verify the results.

  Scenario: Searching for QA Automation Tools
    Given User opens the Google homepage
    When User search for "QA Automation Tools"
    Then User should see search results

  Scenario: Verifying the News Tab on Google
    Given User opens the Google homepage
    When User search for "QA Automation Tools"
    And User click the News tab
    Then User should see news articles

Feature: Check Whether news page for blavity Website Blavity.com is appropriate

  Scenario: To check whether News page is as required
      Given url is launched
      When I am on blavity page
      Then check whether page is loaded
      Then verify whether News page is as required
      Then verify footer section is present and displayed
      Then close the browser

#  Scenario: To check whether Op-Eds page is as required
 #     Given url is launched
  #    When I am on blavity page
   #   Then check whether page is loaded
    #  Then verify whether Op-Eds page is as required
     # Then close the browser      

#Then verify whether Op-Eds page is as required
      #Then verify whether Lifestyle page is as required
      #Then verify whether Culture page is as required
      #Then verify whether Politics page is as required
      #Then verify footer section is present and displayed
      #Then close the browser

 # Examples: 
  #     | page |
   #    | News |
    #   | Op-Eds |
     #  | Lifestyle |
      # | Culture |
       #| Politics |
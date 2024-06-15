Page allows users collection of survey data from varying number of structured questions.

Functionality implemented so far (initial commit):

+user registration, role assignment

+user login, with separate user pages based on roles

+import of queries from file

+export of answers to spreadsheet

+user account management from admin page

+user survey feature. page supports dynamic expansion to allow unlimited number of questions, currently formatted to use 3-option dropdown* for answers

+bootstrap modals implemented to notify of succesful or failed operations

*Base requirement for this project due to need to automatically process the answers for any given question from both user and manager according to pre-determined logic. 
Otherwise, moving answer processing logic to separate module and adding open questions would be a logical next step.

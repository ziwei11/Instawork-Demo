# Instawork-Demo

## Time spent on this project

6 hours

## To run the demo:
1. `pip3 install pipenv`
2. `pipenv shell`
3. `pipenv install django`
4. `cd teammembers`
5. `python manage.py migrate`
6. `python manage.py runserver`

## What it does
The project is to implement a simple team-member management application that allows the user to view, edit, add, and delete team members. The app consists of 3 pages that are documented below:

<img width="553" alt="截屏2023-02-04 下午6 07 57" src="https://user-images.githubusercontent.com/59899776/216801550-d11c90ba-773f-4eae-b8de-a164d4906a62.png">

<img width="551" alt="截屏2023-02-04 下午6 08 08" src="https://user-images.githubusercontent.com/59899776/216801557-60c5c3ee-fdd5-44bf-b85d-d3031bf51cc6.png">

<img width="549" alt="截屏2023-02-04 下午6 08 35" src="https://user-images.githubusercontent.com/59899776/216801563-8d24b4aa-bcf1-4e59-9dfd-c3dda9c9ecb9.png">

## List page
This page shows a list of all team members. Note that the subtitle should reflect the number of team members (the screenshot is wrong, it should say 4). Also note that if the team member is an admin, that is listed next to their name. Clicking a team member should show the Edit page. Clicking the plus at the top should show the Add page.

## Add page
The Add page appears when the user clicks the "+" on the List page. The user enters a team member's first & last name, their phone number, and email. Additionally, they can choose the team member's role (it defaults to regular). Hitting save adds the team member to the list and shows the List page.

## Edit page
The Edit page appears when the user clicks a team member on the List page. This shows a form where the user can edit the details of the team member, including changing their role. Clicking save edits the team member information and shows the List page. Clicking Delete removes the team member and returns to the List page.

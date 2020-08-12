![alt text](https://m0m0-d3v.github.io/img/meetmarketprezi.png "meetmarketprezi")

# This is a group project about improving Craigslist

#### Meet the team:
- Sawyee Beck
- Levi Blank
- Patrick Hebert
- Monica Hong

### Our goal is to build a better functioning Craigslist using Python / Django! We like the simplicity and broad spectrum of what Craigslist offers, but we cringe at their design approach because it looks like everything is thrown in together-- It's way too busy! Our focus was to clean with a minimalistic approach.

#### MeetMarket was built in 5 days- 2 days of planning and 3 days of coding.
In that time, we were able to achieve our **MVP** of:
* [x] Login / Reg with front-end html validations and back-end with bcrypt
* [x] Front page algorithm to show the 3 newest categories
* [x] Users can post new listings
  * [x] Images can be uploaded 
* [x] Users can edit and delete their own postings
* [x] Message system that users can leave the poster questions and comments
* [x] Profile pages for users with details of their membership and their Listing history
* [x] Postings can be 'flagged' for abuse by other users for review by Admin
* [x] Admin level views of all user pages with special controls to edit or delete
* [x] Custom built Admin control hub with full control
  * [x] Create / Edit / or Delete categories
  * [x] Edit or Remove users
  * [x] Review Posts marked 'flagged' and take actions to edit or delete
  * [x] Overview all Postings and options for edit and delete

# Current progress in further development!
#### To-Do List
* [x] DRY to Base htmls
* [x] Setup namespace and named url paths
* [x] Change any existing url pathing to the namedpaths for professional looking code
* [ ] Rewrite the algorithm for "Last 3 Categories" on front page..
  * [ ] Should be Newest Categories that correlate to the 3 Newest Listings added
* [ ] Item Info Page
  * [ ] Resize Pics to 200x200
  * [ ] Listing Info Side by side with Messaging / Comments
* [ ] User Info Page
  * [ ] Fix Avg Rating
* [ ] Admin Control Page
  * [ ] Side by side column for All Categories and All Users
  * [ ] Pagination to 10 Items for all tables
  * [ ] Sortable tables
* [ ] Direct Messaging System
  * [ ] On this_user page, Send Message to this_user from session_user
  * [ ] Add to NavBar
  * [ ] Direct Message Page to retrieve messages
* [ ] Google Maps API

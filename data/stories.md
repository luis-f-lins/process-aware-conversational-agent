## get back on track
* out_of_scope
    - utter_default_fallback

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
    - action_listen

## request list
* request_todolist
    - utter_tasklist
    - utter_book_flight
<!-- 
## book flight
* booking_flight
    - utter_okay
    - action_listen
* flight_booked
    - flight_booked
    - slot{"flight_booked": true}
    - whats_left
    - action_listen

## book hotel after flight
* booking_hotel
    - slot{"flight_booked": true}
    - utter_okay
    - action_listen
* hotel_booked
    - hotel_booked
    - slot{"hotel_booked": true}
    - whats_left
    - action_listen

## book hotel before flight
* booking_hotel
    - slot{"flight_booked": false}
    - utter_book_flight

## book transfer before flight
* booking_transfer
    - slot{"flight_booked": false}
    - slot{"hotel_booked": false}
    - utter_book_flight_and_hotel

## book transfer before hotel
* booking_transfer
    - slot{"hotel_booked": false}
    - utter_book_hotel

## book transfer after flight and hotel
* booking_transfer
    - slot{"flight_booked": true}
    - slot{"hotel_booked": true}
    - utter_okay
    - action_listen
* transfer_booked
    - transfer_booked
    - slot{"transfer_booked": true}
    - whats_left
    - action_listen


## book tour before flight
* booking_tour
    - slot{"flight_booked": false}
    - utter_book_flight

## book tour after flight
* booking_tour
    - slot{"flight_booked": true}
    - utter_okay
    - action_listen
* tour_booked
    - tour_booked
    - slot{"tour_booked": true}
    - whats_left
    - action_listen -->
<!-- 
## interactive_story_1
* request_todolist
    - utter_tasklist
    - utter_book_flight
* booking_flight
    - utter_okay
* flight_booked
    - flight_booked
    - slot{"flight_booked": true}
    - whats_left

## something_booked_flight
* booking_flight
  - utter_okay
  - action_listen
* something_booked
  - flight_booked
  - slot{"flight_booked": true}
  - whats_left
  - action_listen

## something_booked_hotel
* booking_hotel
  - slot{"flight_booked": true}
  - utter_okay
  - action_listen
* something_booked
  - hotel_booked
  - slot{"hotel_booked": true}
  - whats_left
  - action_listen

## something_booked_transfer
* booking_transfer
  - slot{"flight_booked": true}
  - slot{"hotel_booked": true}
  - utter_okay
  - action_listen
* something_booked
  - transfer_booked
  - slot{"transfer_booked": true}
  - whats_left
  - action_listen

## something_booked_tour
* booking_tour
  - slot{"flight_booked": true}
  - utter_okay
  - action_listen
* something_booked
  - tour_booked
  - slot{"tour_booked": true}
  - whats_left
  - action_listen -->

<!-- ## interactive_story_1
* request_todolist
    - utter_tasklist
    - utter_book_flight
* booking_flight
    - utter_okay
* booking_tour
    - utter_book_flight
* booking_hotel
    - utter_book_flight
* booking_transfer
    - utter_book_flight_and_hotel
* booking_flight
    - utter_okay
* flight_booked
    - flight_booked
    - slot{"flight_booked": true}
    - whats_left
* booking_transfer
    - utter_book_hotel -->

## booked flight
* flight_booked
    - flight_booked
    - whats_left

## booked hotel without notice
* hotel_booked
    - hotel_booked
    - slot{"hotel_booked": false} 
    - action_listen

## booked transfer without notice
* transfer_booked
    - transfer_booked
    - slot{"transfer_booked": false}
    - action_listen

## booked tour without notice
* tour_booked
    - tour_booked
    - slot{"tour_booked": false}
    - action_listen

## booked hotel without notice
* hotel_booked
    - hotel_booked
    - slot{"hotel_booked": true} 
    - whats_left

## booked transfer without notice
* transfer_booked
    - transfer_booked
    - slot{"transfer_booked": true}
    - whats_left

## booked tour without notice
* tour_booked
    - tour_booked
    - slot{"tour_booked": true}
    - whats_left

## now what
* now_what
    - whats_left

<!-- ## interactive_story_1
* request_todolist
    - utter_tasklist
    - utter_book_flight
* transfer_booked
    - transfer_booked
* booking_transfer
    - utter_book_flight_and_hotel
* booking_hotel
    - utter_book_flight
* hotel_booked
    - hotel_booked
* booking_flight
    - utter_okay
* flight_booked
    - flight_booked
    - slot{"flight_booked": true}
    - whats_left
* tour_booked
    - tour_booked
    - slot{"tour_booked": true} -->
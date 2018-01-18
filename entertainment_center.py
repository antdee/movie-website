#!/usr/bin/env python2.7
# -*- coding: ascii -*-

"""
This module will collect details for the movies and series
to be listed on the movie trailer website.
In the end it will call the function from the fresh_tomatoes.py module
create the html code and open it on the browser.
"""

import fresh_tomatoes

import media

import datetime

toy_story = media.Movie(
 "Toy Story",
 str(datetime.timedelta(seconds=4860)),
 "A story of a boy",
 "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
 "https://youtu.be/KYz2wyBy3kc",
 "March 22, 1996",
 "8.3/10 IMDb")

avatar = media.Movie(
 "Avatar",
 str(datetime.timedelta(seconds=9720)),
 "A marine on an alien planet",
 "https://goo.gl/ZQ42JE",
 "https://youtu.be/5PSNL1qE6VY",
 "December 18, 2009",
 "7.8/10 IMDb")

the_avengers = media.Movie(
 "The Avengers",
 str(datetime.timedelta(seconds=8580)),
 "Supeheroes and stuff...",
 "https://images-na.ssl-images-amazon.com/images/I/71%2BNoq4xpNL._SL1001_.jpg",
 "https://youtu.be/eOrNdBpGMv8",
 "April 11, 2012",
 "8.1/10 IMDb")

school_of_rock = media.Movie(
 "School of Rock",
 str(datetime.timedelta(seconds=6540)),
 "Kids playing music and all that",
 "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
 "https://youtu.be/XCwy6lW5Ixc",
 "February 6, 2004",
 "7.1/10 IMDb")

ratatouille = media.Movie(
 "Ratatouille",
 str(datetime.timedelta(seconds=6660)),
 "A rat cooking",
 "https://images-na.ssl-images-amazon.com/images/I/71VDlRubWtL._SY550_.jpg",
 "https://youtu.be/c3sBBRxDAqk",
 "June 28, 2007",
 "8/10 IMDb")

midnight_in_paris = media.Movie(
 "Midnight in Paris",
 str(datetime.timedelta(seconds=6000)),
 "Paris in the middle of the night",
 "https://goo.gl/J39d9r",
 "https://youtu.be/FAfR8omt-CY",
 "October 7, 2011",
 "7.7/10 IMDb")

hunger_games = media.Movie(
 "The Hunger Games",
 str(datetime.timedelta(seconds=8520)),
 "Hungry people fighting???",
 "https://goo.gl/DFUvYF",
 "https://youtu.be/mfmrPu43DF8",
 "March 23, 2012",
 "7.3/10 IMDb")

lotr_1 = media.Movie(
 "The Lord of the Rings: The Fellowship of the Ring",
 str(datetime.timedelta(seconds=13680)),
 "Middle-earth",
 "https://goo.gl/wv3hc4",
 "https://youtu.be/V75dMMIW2B4",
 "December 19, 2001",
 "8.8/10 IMDb")

lotr_2 = media.Movie(
 "The Lord of the Rings: The Two Towers",
 str(datetime.timedelta(seconds=14100)),
 "The sequel,'",
 "https://goo.gl/hZ1qwR",
 "https://youtu.be/LbfMDwc4azU",
 "December 18, 2002",
 "8.7/10 IMDb")

lotr_3 = media.Movie(
 "The Lord of the Rings: The Return of the King",
 str(datetime.timedelta(seconds=14100)),
 "It is the third and final installment in The Lord of the Rings trilogy",
 "https://goo.gl/UAeTR3",
 "https://youtu.be/r5X-hFf6Bwo",
 "December 17, 2003",
 "8.9/10 IMDb")

ray_donovan = media.Serie(
 "Ray Donovan",
 "Season 1",
 "Ray Donovan",
 "12 Episodes",
 "Ray Donovan is a 'fixer' for the powerful law firm Goldman & Drexler,"
 "representing the rich and famous of Los Angeles, California.",
 "http://cdn.putlockers.fm/ebLiMkG.jpg",
 "https://youtu.be/r36OT6TsHOw",
 "June 30, 2013",
 "9.0/10 IMDb")

ray_don_s1_e1 = media.Serie(
 "Ray Donovan",
 "S1Ep01",
 "The Bag or the Bat",
 str(datetime.timedelta(seconds=3540)),
 "Ray Donovan fixes problems for a powerful LA law firm. Originally from South"
 "Boston, he now lives in the affluent city of Calabasas, California.",
 "https://goo.gl/DbgWSp",
 "https://youtu.be/YISeuBninSk",
 "June 30, 2013",
 "8.1/10 IMDb")

ray_don_s1_e2 = media.Serie(
 "Ray Donovan",
 "S1Ep02",
 "A Mouth Is a Mouth",
 str(datetime.timedelta(seconds=3180)),
 "Ray tries to send Mickey back to prison. Angry with Ray,"
 "Abby allows her kids to spend the day with Mickey. Ray handles two crises.",
 "https://goo.gl/hQoV5k",
 "https://youtu.be/maxnpKE-3rk",
 "July 7, 2013",
 "8.1/10 IMDb")

ray_don_s1_e3 = media.Serie(
 "Ray Donovan",
 "S1Ep03",
 "Twerk",
 str(datetime.timedelta(seconds=3240)),
 "Mickey spends time with his sons. Ray 'buys' a talented hip-hop  artist,"
 "Marvin Gaye Washington, for his rapper neighbor. Bridget becomes friendly.",
 "https://goo.gl/VPggq9",
 "https://youtu.be/eUDYiKDrL2I",
 "July 14, 2013",
 "8.1/10 IMDb")


ray_don_s1_e4 = media.Serie(
 "Ray Donovan",
 "S1Ep04",
 "Black Cadillac",
 str(datetime.timedelta(seconds=2940)),
 "Ray is forced by Abby to visit Bel Air Academy to see Bridget's potential"
 "school, while trying to deal with a work situation. Mickey meets his ex.",
 "https://goo.gl/GyHvar",
 "https://youtu.be/JWBNQ8o5sh0",
 "July 21, 2013",
 "8.1/10 IMDb")

ray_don_s1_e5 = media.Serie(
 "Ray Donovan",
 "S1Ep05",
 "The Golem",
 str(datetime.timedelta(seconds=3120)),
 "The three Donovan brothers remember the anniversary of their sister's "
 " demise. Ray and Avi get the money back that Bunchy spent on his house.",
 "https://goo.gl/pNj9Ej",
 "https://youtu.be/NbahJbClVvA",
 "July 28, 2013",
 "8.1/10 IMDb")

ray_don_s1_e6 = media.Serie(
 "Ray Donovan",
 "S1Ep06",
 "Housewarming",
 str(datetime.timedelta(seconds=3100)),
 "Bunchy receives his money from the settlement with the Church. Mickey"
 "and Ezra reminisce events while Mickey wears a wire. Ezra has an accident.",
 "https://goo.gl/ZjHS1A",
 "https://youtu.be/gu2Xg5Msn0g",
 "August 4, 2013",
 "8.1/10 IMDb")

ray_don_s1_e7 = media.Serie(
 "Ray Donovan",
 "S1Ep07",
 "New Birthday",
 str(datetime.timedelta(seconds=3180)),
 "Ray tries to shut down Van Miller's investigation by drugging him, and"
 "using this to create an incriminating video. Bunchy throws a party.",
 "https://goo.gl/vQsWNq",
 "https://youtu.be/Hv9onuAlO0s",
 "August 11, 2013",
 "8.1/10 IMDb")


ray_don_s1_e8 = media.Serie(
 "Ray Donovan",
 "S1Ep08",
 "Bridget",
 str(datetime.timedelta(seconds=3185)),
 "Ray finds out about Bridget's relationship with Marvin and forbids"
 "her from seeing him, but she visits him anyway, leading to emotional upset.",
 "https://goo.gl/fdQuMw",
 "https://youtu.be/gCIQ3WJk7-E",
 "September 8, 2013",
 "8.1/10 IMDb")


ray_don_s1_e9 = media.Serie(
 "Ray Donovan",
 "S1Ep09",
 "Road Trip",
 str(datetime.timedelta(seconds=3065)),
 "The Donovans attend Daryll's fight at Terry's club. Meanwhile, Ray's deal"
 "with Sully is put into action. Mickey has a rendezvous. Bunchy encounters",
 "https://goo.gl/PnXbMH",
 "https://youtu.be/-lY6hzcz2xg",
 "August 18, 2013",
 "8.1/10 IMDb")


ray_don_s1_e10 = media.Serie(
 "Ray Donovan",
 "S1Ep10",
 "Fite Nite",
 str(datetime.timedelta(seconds=3022)),
 "Accepting Ray's offer to kill Mickey, Sully travels to Los Angeles,"
 "but the journey does not go as planned, Avi steps in. Asked by Coner",
 "https://goo.gl/ULoYNM",
 "https://youtu.be/FSGUoaaP9Cc",
 "August 25, 2013",
 "8.1/10 IMDb")


ray_don_s1_e11 = media.Serie(
 "Ray Donovan",
 "S1Ep11",
 "Bucky Fuckn' Dent",
 str(datetime.timedelta(seconds=3189)),
 "Horrible secrets are revealed when the Donovan boys encounter the"
 "priest who abused Bunchy and Ray when they were boys. Ray executes him.",
 "https://goo.gl/UWwxGP",
 "https://youtu.be/yQUgBfGzzDI",
 "September 8, 2013",
 "8.1/10 IMDb")


ray_don_s1_e12 = media.Serie(
 "Ray Donovan",
 "S1Ep12",
 "Same Exactly",
 str(datetime.timedelta(seconds=3290)),
 "With Sully on the run, Ray suggests to Frank a bold strategy in finding him;"
 "Abby leaves Ray a heartfelt message; Lena convinces Bridget to forgive.",
 "https://goo.gl/pw6nYq",
 "https://youtu.be/AvzK1oCJ2Yg",
 "September 22, 2013",
 "8.1/10 IMDb")

# Add a movie or a serie to the appropriate list after defining it above.
movies = [ 
 toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,
 hunger_games, lotr_1, lotr_2, lotr_3]

series = [
 ray_donovan, ray_don_s1_e1, ray_don_s1_e2, ray_don_s1_e3, ray_don_s1_e4,
 ray_don_s1_e5, ray_don_s1_e6, ray_don_s1_e7, ray_don_s1_e8, ray_don_s1_e9,
 ray_don_s1_e10, ray_don_s1_e11, ray_don_s1_e12]


fresh_tomatoes.open_movies_page(movies, series)

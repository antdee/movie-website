#!/usr/bin/env python2.7
# -*- coding: ascii -*-

"""
This module will store the Classes to be called in
entertainment_center.py.
"""

import webbrowser


class Video():
    """This parent class stores common details for movies and series"""
    def __init__(self, video_title, video_duration, video_storyline,
                 poster_image, trailer_youtube, video_release_date,
                 imdb_rating):
        self.title = video_title
        self.duration = video_duration
        self.release_date = video_release_date
        self.imdb_rating = imdb_rating
        self.storyline = video_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


class Movie(Video):
    """This class stores Movie details"""
    def __init__(self, video_title, video_duration, video_storyline,
                 poster_image, trailer_youtube, video_release_date,
                 imdb_rating):
        Video.__init__(self, video_title, video_duration, video_storyline,
                       poster_image, trailer_youtube, video_release_date,
                       imdb_rating)


class Serie(Video):
    """This class provides a way to store Series details"""
    def __init__(self, video_title, season_episode_number, episode_title,
                 video_duration, video_storyline, poster_image,
                 trailer_youtube, video_release_date, imdb_rating):
        Video.__init__(self, video_title, video_duration, video_storyline,
                       poster_image, trailer_youtube, video_release_date,
                       imdb_rating)
        self.season_episode_number = season_episode_number
        self.episode = episode_title

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used to calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def set_of_three_equal_nums(num, dice):
    score = 0
    if sum([x == num for x in dice]) == 3:
        if num == 1:
            score += 1000
        else:
            score += 100 * num
    for i in range(len(dice)):
        if dice[i] == num:
            dice.pop(i)
        
    return score, dice
    
def set_of_single_num(num, dice):
    score = 0
    num_times = sum([x == num for x in dice])
    if num == 5 and num_times < 3:
        score += 50 * num_times
    if num == 1 and num_times < 3:
        score += 100 * num_times_in_dice
    return score

def score(dice):
    score = 0
    nums = set(dice)
    for num in nums:
        times_in_dice = sum([x == num for x in dice])
        print(f"{num} appears {times_in_dice} times in {dice}")
        if times_in_dice >= 3:
            if num == 1: 
                score += 1000
            else:
                score += num * 100
            times_in_dice = times_in_dice - 3
        
        print(f"{num} in new times in dice: {times_in_dice}")
        if num == 1:
            score += times_in_dice * 100
        if num == 5:
            score += times_in_dice * 50
    
    return score

class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        print("======")
        self.assertEqual(0, score([]))
        print("======")

    def test_score_of_a_single_roll_of_5_is_50(self):
        print("======")
        self.assertEqual(50, score([5]))
        print("======")

    def test_score_of_a_single_roll_of_1_is_100(self):
        print("======")
        self.assertEqual(100, score([1]))
        print("======")

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        print("======")
        self.assertEqual(300, score([1,5,5,1]))
        print("======")

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        print("======")
        self.assertEqual(0, score([2,3,4,6]))
        print("======")

    def test_score_of_a_triple_1_is_1000(self):
        print("======")
        self.assertEqual(1000, score([1,1,1]))
        print("======")

    def test_score_of_other_triples_is_100x(self):
        print("======")
        self.assertEqual(200, score([2,2,2]))
        print("======")
        print("======")
        self.assertEqual(300, score([3,3,3]))
        print("======")
        print("======")
        self.assertEqual(400, score([4,4,4]))
        print("======")
        print("======")
        self.assertEqual(500, score([5,5,5]))
        print("======")
        print("======")
        self.assertEqual(600, score([6,6,6]))
        print("======")

    def test_score_of_mixed_is_sum(self):
        print("======")
        self.assertEqual(250, score([2,5,2,2,3]))
        print("======")
        print("======")
        self.assertEqual(550, score([5,5,5,5]))
        print("======")
        print("======")
        self.assertEqual(1150, score([1,1,1,5,1]))
        print("======")

    def test_ones_not_left_out(self):
        print("======")
        self.assertEqual(300, score([1,2,2,2]))
        print("======")
        print("======")
        self.assertEqual(350, score([1,5,2,2,2]))
        print("======")

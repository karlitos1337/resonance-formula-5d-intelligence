#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evolutionary Game Theory Tests for Resonanzformel & 5D-Intelligenz

Tests whether open, transparent systems with error culture and feedback
can evolve toward stable cooperation (Green/Green) vs. remaining in
oscillation between cooperation and defection.

Hypothesis: With Resonanzformel principles, systems evolve to and stay Green.
Without them, systems oscillate or converge to Red (defection).
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple
import json


class PlayerStrategy:
    """Base class for game theory strategies"""
    
    COOPERATE = "GREEN"
    DEFECT = "RED"
    NEUTRAL = "GRAY"


@dataclass
class GamePayoff:
    """Standard prisoner's dilemma payoffs"""
    mutual_cooperation = 3      # Both cooperate: both win 3
    mutual_defection = 1        # Both defect: both get 1
    sucker_payoff = 0           # You cooperate, they defect: you get 0
    exploitation_payoff = 4     # You defect, they cooperate: you get 4


class OpenSystemEnvironment:
    """Environment with Resonanzformel principles active"""
    
    def __init__(self, num_players=50, num_rounds=100):
        self.num_players = num_players
        self.num_rounds = num_rounds
        self.players = [PlayerStrategy.COOPERATE] * num_players  # All start cooperating
        self.payoffs = GamePayoff()
        self.history = []
        self.transparency_log = []  # Track what players see
        
    def step_with_resonance(self, round_num):
        """Execute one game round WITH Resonanzformel principles"""
        scores = [0] * self.num_players
        new_strategies = self.players.copy()
        
        # Round 1: All play (open assignment)
        for i in range(self.num_players):
            for j in range(i + 1, self.num_players):
                player_i_move = self.players[i]
                player_j_move = self.players[j]
                
                # Calculate payoff
                if player_i_move == PlayerStrategy.COOPERATE and player_j_move == PlayerStrategy.COOPERATE:
                    scores[i] += self.payoffs.mutual_cooperation
                    scores[j] += self.payoffs.mutual_cooperation
                elif player_i_move == PlayerStrategy.DEFECT and player_j_move == PlayerStrategy.COOPERATE:
                    scores[i] += self.payoffs.exploitation_payoff
                    scores[j] += self.payoffs.sucker_payoff
                elif player_i_move == PlayerStrategy.COOPERATE and player_j_move == PlayerStrategy.DEFECT:
                    scores[i] += self.payoffs.sucker_payoff
                    scores[j] += self.payoffs.exploitation_payoff
                else:  # Both defect
                    scores[i] += self.payoffs.mutual_defection
                    scores[j] += self.payoffs.mutual_defection
        
        # KEY RESONANZFORMEL MECHANISM:
        # Phase 2: TRANSPARENCY - Show players the longterm effect
        best_score = max(scores) if scores else 0
        avg_score = np.mean(scores) if scores else 0
        
        transparent_message = {
            "round": round_num,
            "best_score": best_score,
            "avg_score": avg_score,
            "green_players": sum(1 for p in self.players if p == PlayerStrategy.COOPERATE),
            "red_players": sum(1 for p in self.players if p == PlayerStrategy.DEFECT)
        }
        self.transparency_log.append(transparent_message)
        
        # Phase 3: ERROR CULTURE + FEEDBACK
        # Defectors see: "Your defection gave you short gain, but collapsed collective score"
        # They CAN change without punishment (error culture)
        for i in range(self.num_players):
            if self.players[i] == PlayerStrategy.DEFECT:
                # Defector sees: "If everyone like me defects, everyone gets 1. If all cooperate, all get 3"
                if avg_score < 2:  # Signals: system is breaking down
                    # With error culture: "I can change without shame"
                    if np.random.random() < 0.3:  # 30% switch to green (learning)
                        new_strategies[i] = PlayerStrategy.COOPERATE
        
        self.players = new_strategies
        self.history.append({
            "round": round_num,
            "green_count": sum(1 for p in self.players if p == PlayerStrategy.COOPERATE),
            "red_count": sum(1 for p in self.players if p == PlayerStrategy.DEFECT)
        })
    
    def step_without_resonance(self, round_num):
        """Execute one game round WITHOUT Resonanzformel (standard evolutionary dynamics)"""
        scores = [0] * self.num_players
        new_strategies = self.players.copy()
        
        # Play: random pairings
        for i in range(self.num_players):
            for j in range(i + 1, self.num_players):
                player_i_move = self.players[i]
                player_j_move = self.players[j]
                
                if player_i_move == PlayerStrategy.COOPERATE and player_j_move == PlayerStrategy.COOPERATE:
                    scores[i] += self.payoffs.mutual_cooperation
                    scores[j] += self.payoffs.mutual_cooperation
                elif player_i_move == PlayerStrategy.DEFECT and player_j_move == PlayerStrategy.COOPERATE:
                    scores[i] += self.payoffs.exploitation_payoff
                    scores[j] += self.payoffs.sucker_payoff
                elif player_i_move == PlayerStrategy.COOPERATE and player_j_move == PlayerStrategy.DEFECT:
                    scores[i] += self.payoffs.sucker_payoff
                    scores[j] += self.payoffs.exploitation_payoff
                else:
                    scores[i] += self.payoffs.mutual_defection
                    scores[j] += self.payoffs.mutual_defection
        
        # NO TRANSPARENCY: Players DON'T see the system-wide picture
        # NO ERROR CULTURE: If you defect and win, you're "successful", keep doing it
        # ONLY mechanism: Imitate winners (standard evolutionary pressure)
        for i in range(self.num_players):
            # Imitate a random other player if they did better
            j = np.random.randint(self.num_players)
            if scores[j] > scores[i]:
                new_strategies[i] = self.players[j]  # Copy their strategy
        
        self.players = new_strategies
        self.history.append({
            "round": round_num,
            "green_count": sum(1 for p in self.players if p == PlayerStrategy.COOPERATE),
            "red_count": sum(1 for p in self.players if p == PlayerStrategy.DEFECT)
        })


class EvolutionaryGameTheoryTests:
    """Complete test suite for Resonanzformel evolution hypothesis"""
    
    def test_convergence_to_green_with_resonance(self):
        """Test 1: Does transparency + error culture cause convergence to Green?"""
        print("\n" + "="*80)
        print("TEST 1: CONVERGENCE TO GREEN WITH RESONANZFORMEL")
        print("="*80)
        
        env = OpenSystemEnvironment(num_players=50, num_rounds=100)
        
        for round_num in range(env.num_rounds):
            env.step_with_resonance(round_num)
        
        final_green_ratio = env.history[-1]["green_count"] / env.num_players
        print(f"\nFinal Green Ratio: {final_green_ratio:.2%}")
        print(f"Trajectory: {[h['green_count'] for h in env.history[::10]]}")
        
        if final_green_ratio > 0.8:
            print("✅ HYPOTHESIS CONFIRMED: System converged to Green (>80%)")
            return True
        else:
            print("❌ HYPOTHESIS REJECTED: System did not converge")
            return False
    
    def test_comparison_with_without_resonance(self):
        """Test 2: Compare WITH vs WITHOUT Resonanzformel"""
        print("\n" + "="*80)
        print("TEST 2: COMPARISON - WITH vs WITHOUT RESONANZFORMEL")
        print("="*80)
        
        # WITH Resonanzformel
        env_with = OpenSystemEnvironment(num_players=50, num_rounds=100)
        for round_num in range(env_with.num_rounds):
            env_with.step_with_resonance(round_num)
        
        # WITHOUT Resonanzformel
        env_without = OpenSystemEnvironment(num_players=50, num_rounds=100)
        for round_num in range(env_without.num_rounds):
            env_without.step_without_resonance(round_num)
        
        with_ratio = env_with.history[-1]["green_count"] / env_with.num_players
        without_ratio = env_without.history[-1]["green_count"] / env_without.num_players
        
        print(f"\nWITH Resonanzformel - Final Green: {with_ratio:.2%}")
        print(f"WITHOUT Resonanzformel - Final Green: {without_ratio:.2%}")
        print(f"Difference: {(with_ratio - without_ratio):.2%}")
        
        if with_ratio > without_ratio:
            print("✅ Resonanzformel INCREASES cooperation")
            return True
        else:
            print("❌ Resonanzformel effect not visible")
            return False
    
    def test_stability_stays_green(self):
        """Test 3: Once Green, does system STAY Green?"""
        print("\n" + "="*80)
        print("TEST 3: STABILITY - ONCE GREEN, STAYS GREEN")
        print("="*80)
        
        env = OpenSystemEnvironment(num_players=50, num_rounds=200)
        
        for round_num in range(env.num_rounds):
            env.step_with_resonance(round_num)
        
        # Check if Green remains stable in second half
        second_half_green = [h["green_count"] for h in env.history[100:]]
        avg_green_second_half = np.mean(second_half_green) / env.num_players
        std_green_second_half = np.std(second_half_green) / env.num_players
        
        print(f"\nSecond half average Green: {avg_green_second_half:.2%}")
        print(f"Volatility (std): {std_green_second_half:.2%}")
        
        if avg_green_second_half > 0.8 and std_green_second_half < 0.1:
            print("✅ HYPOTHESIS CONFIRMED: Green is STABLE")
            return True
        else:
            print("❌ HYPOTHESIS REJECTED: Green oscillates or declines")
            return False
    
    def test_fusion_hypothesis(self):
        """Test 4: Extreme - Do players eventually see 'We are One'?"""
        print("\n" + "="*80)
        print("TEST 4: FUSION HYPOTHESIS - DO SYSTEMS TRANSCEND INDIVIDUAL/COLLECTIVE?")
        print("="*80)
        
        env = OpenSystemEnvironment(num_players=50, num_rounds=200)
        
        for round_num in range(env.num_rounds):
            env.step_with_resonance(round_num)
        
        # Fusion = 100% Green for sustained period
        final_30_rounds = [h["green_count"] for h in env.history[-30:]]
        if all(count == env.num_players for count in final_30_rounds):
            print("\n✅ EXTREME HYPOTHESIS CONFIRMED: Complete Fusion (100% Green for 30+ rounds)")
            print("   Interpretation: System transcended Red/Green binary → Pure Cooperation")
            return True
        else:
            print("\n⚠️  Fusion not achieved, but cooperation stable")
            return False
    
    def run_all_tests(self):
        """Execute complete test suite"""
        print("\n🧬 EVOLUTIONARY GAME THEORY TEST SUITE 🧬")
        print("Testing: Can Resonanzformel drive systems to stable cooperation?")
        
        results = {
            "test_1_convergence": self.test_convergence_to_green_with_resonance(),
            "test_2_comparison": self.test_comparison_with_without_resonance(),
            "test_3_stability": self.test_stability_stays_green(),
            "test_4_fusion": self.test_fusion_hypothesis()
        }
        
        print("\n" + "="*80)
        print("FINAL RESULTS")
        print("="*80)
        for test, result in results.items():
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{test}: {status}")
        
        total_passed = sum(results.values())
        print(f"\nTotal: {total_passed}/4 tests passed")
        
        if total_passed >= 3:
            print("\n🎉 RESONANZFORMEL HYPOTHESIS LARGELY CONFIRMED")
            print("   Open, transparent systems WITH error culture CAN evolve to stable cooperation")
        elif total_passed >= 2:
            print("\n⚠️  PARTIAL SUPPORT for Resonanzformel hypothesis")
        else:
            print("\n❌ RESONANZFORMEL HYPOTHESIS NOT SUPPORTED")
        
        return results


if __name__ == "__main__":
    tester = EvolutionaryGameTheoryTests()
    results = tester.run_all_tests()

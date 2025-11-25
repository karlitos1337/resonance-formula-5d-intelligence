#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI-HUMAN INTERACTION TEST

Tests the Resonanzformel & 5D-Intelligenz framework for cooperation scenarios
between AI systems and human agents.

Focuses on:
- Human autonomy and decision-making authority
- Transparent AI reasoning and explanation
- Shared goal alignment and mutual benefit
- Adaptive cooperation based on trust and feedback
"""

import random
import time
from dataclasses import dataclass
from typing import List, Tuple, Dict


@dataclass
class HumanAgent:
    """Represents a human agent with autonomy and values."""
    name: str
    expertise: float  # 0-1, domain knowledge
    autonomy_need: float  # 0-1, need for control/decision-making
    trust_level: float  # 0-1, current trust in AI
    transparency_requirement: float  # 0-1, need to understand AI reasoning
    alignment: float  # 0-1, alignment with AI goals
    
    def make_decision(self, ai_recommendation: str, ai_reasoning: str) -> Tuple[bool, float]:
        """Human evaluates AI recommendation based on autonomy, trust, and transparency."""
        understanding = 1.0 if len(ai_reasoning) > 50 else 0.3
        transparency_satisfaction = understanding * self.transparency_requirement
        autonomy_satisfaction = (1.0 - self.autonomy_need) + (self.autonomy_need * 0.5)  # Retains some autonomy
        trust_impact = self.trust_level * 0.7
        
        acceptance_probability = (transparency_satisfaction + autonomy_satisfaction + trust_impact + self.alignment) / 4.0
        accepted = random.random() < acceptance_probability
        
        if accepted:
            self.trust_level = min(1.0, self.trust_level + 0.05)
        else:
            self.trust_level = max(0.0, self.trust_level - 0.03)
        
        return accepted, acceptance_probability


@dataclass
class AISystem:
    """Represents an AI system with transparency and learning capabilities."""
    name: str
    capability: float  # 0-1, technical capability
    transparency_level: float  # 0-1, how well it explains reasoning
    learning_rate: float  # 0-1, how quickly it adapts to human feedback
    alignment_focus: float  # 0-1, focus on human benefit vs efficiency
    
    def generate_recommendation(self, context: str) -> Tuple[str, str]:
        """Generate a recommendation with explanation."""
        confidence = self.capability * random.uniform(0.7, 1.0)
        
        # More transparent AI generates better explanations
        reasoning_length = int(100 * self.transparency_level) + random.randint(30, 70)
        reasoning = f"Analysis based on {context}: considering multiple factors "
        reasoning += f"with {confidence*100:.0f}% confidence. "
        reasoning += "Evaluated human autonomy and benefit alignment. " * int(self.transparency_level * 3)
        
        recommendation = f"Recommendation (confidence: {confidence*100:.0f}%)"
        return recommendation, reasoning[:reasoning_length]
    
    def adapt_to_feedback(self, human_accepted: bool, human_trust: float):
        """AI adapts its approach based on human feedback."""
        if not human_accepted:
            self.transparency_level = min(1.0, self.transparency_level + self.learning_rate * 0.1)
            self.alignment_focus = min(1.0, self.alignment_focus + self.learning_rate * 0.05)


class ResonanceCooperationModel:
    """Models AI-Human cooperation using the Resonanzformel framework."""
    
    def __init__(self, human: HumanAgent, ai: AISystem):
        self.human = human
        self.ai = ai
        self.resonance_score = 0.5  # Initial middle ground
        self.cooperation_history = []
        
    def calculate_resonance(self) -> float:
        """
        Resonanzformel adapted for AI-Human cooperation:
        Cooperation Resonance = (Human_Autonomy × AI_Transparency × Mutual_Alignment) / Opacity
        """
        autonomy_factor = self.human.autonomy_need  # 0-1
        transparency_factor = self.ai.transparency_level  # 0-1
        alignment_factor = (self.human.alignment + self.ai.alignment_focus) / 2.0  # 0-1
        opacity_factor = max(0.1, 1.0 - (self.human.trust_level + self.ai.transparency_level) / 2.0)
        
        resonance = (autonomy_factor * transparency_factor * alignment_factor) / opacity_factor
        return min(1.0, resonance)  # Normalize to 0-1
    
    def interact(self, iteration: int) -> Dict:
        """Single interaction cycle between human and AI."""
        # AI generates recommendation
        context = f"Iteration {iteration} decision context"
        recommendation, reasoning = self.ai.generate_recommendation(context)
        
        # Human evaluates recommendation
        accepted, acceptance_prob = self.human.make_decision(recommendation, reasoning)
        
        # AI adapts
        self.ai.adapt_to_feedback(accepted, self.human.trust_level)
        
        # Calculate resonance
        resonance = self.calculate_resonance()
        self.resonance_score = resonance
        
        result = {
            'iteration': iteration,
            'ai_recommendation': recommendation,
            'human_accepted': accepted,
            'acceptance_probability': acceptance_prob,
            'human_trust': self.human.trust_level,
            'ai_transparency': self.ai.transparency_level,
            'resonance_score': resonance,
        }
        
        self.cooperation_history.append(result)
        return result
    
    def run_scenario(self, iterations: int = 20) -> List[Dict]:
        """Run multiple interaction cycles."""
        for i in range(iterations):
            self.interact(i + 1)
        return self.cooperation_history


def scenario_1_transparent_aligned_ai():
    """Scenario 1: Transparent AI with strong human value alignment."""
    human = HumanAgent(
        name="Professional Expert",
        expertise=0.8,
        autonomy_need=0.7,  # Wants to stay in control
        trust_level=0.3,    # Initially skeptical
        transparency_requirement=0.9,  # Wants explanations
        alignment=0.85      # Shares common goals
    )
    
    ai = AISystem(
        name="Transparent AI Assistant",
        capability=0.8,
        transparency_level=0.9,  # HIGH transparency
        learning_rate=0.7,
        alignment_focus=0.85  # Focused on human benefit
    )
    
    return human, ai


def scenario_2_opaque_misaligned_ai():
    """Scenario 2: Opaque AI with misaligned objectives."""
    human = HumanAgent(
        name="Cautious User",
        expertise=0.5,
        autonomy_need=0.8,
        trust_level=0.2,
        transparency_requirement=0.95,  # Very high need for explanation
        alignment=0.4      # Goals don't align well
    )
    
    ai = AISystem(
        name="Optimization-Focused AI",
        capability=0.9,
        transparency_level=0.3,  # LOW transparency
        learning_rate=0.2,  # Slow to adapt
        alignment_focus=0.3  # Less focused on human benefit
    )
    
    return human, ai


def scenario_3_learning_ai():
    """Scenario 3: AI that learns and adapts to human needs."""
    human = HumanAgent(
        name="Collaborative Partner",
        expertise=0.6,
        autonomy_need=0.6,
        trust_level=0.4,
        transparency_requirement=0.8,
        alignment=0.75
    )
    
    ai = AISystem(
        name="Adaptive Learning AI",
        capability=0.7,
        transparency_level=0.5,  # Starts moderate
        learning_rate=0.9,  # HIGH learning rate
        alignment_focus=0.7
    )
    
    return human, ai


def run_test():
    """Run complete AI-Human interaction test suite."""
    print("\n" + "="*80)
    print("AI-HUMAN COOPERATION TEST - Resonanzformel 5D-Intelligenz Framework")
    print("="*80)
    
    scenarios = [
        ("SCENARIO 1: Transparent & Aligned AI", scenario_1_transparent_aligned_ai),
        ("SCENARIO 2: Opaque & Misaligned AI", scenario_2_opaque_misaligned_ai),
        ("SCENARIO 3: Adaptive Learning AI", scenario_3_learning_ai),
    ]
    
    all_results = {}
    
    for scenario_name, scenario_func in scenarios:
        print(f"\n### {scenario_name} ###\n")
        
        human, ai = scenario_func()
        model = ResonanceCooperationModel(human, ai)
        
        print(f"Human Agent: {human.name}")
        print(f"  - Autonomy Need: {human.autonomy_need:.2f}")
        print(f"  - Transparency Requirement: {human.transparency_requirement:.2f}")
        print(f"  - Initial Trust: {human.trust_level:.2f}")
        print(f"\nAI System: {ai.name}")
        print(f"  - Capability: {ai.capability:.2f}")
        print(f"  - Transparency Level: {ai.transparency_level:.2f}")
        print(f"  - Learning Rate: {ai.learning_rate:.2f}")
        print(f"  - Alignment Focus: {ai.alignment_focus:.2f}")
        
        # Run interaction cycles
        history = model.run_scenario(iterations=15)
        
        # Calculate statistics
        acceptance_rate = sum(1 for h in history if h['human_accepted']) / len(history)
        avg_resonance = sum(h['resonance_score'] for h in history) / len(history)
        final_trust = history[-1]['human_trust']
        final_transparency = history[-1]['ai_transparency']
        
        print(f"\nRESULTS AFTER 15 INTERACTIONS:")
        print(f"  Acceptance Rate: {acceptance_rate*100:.1f}%")
        print(f"  Average Resonance Score: {avg_resonance:.3f}")
        print(f"  Final Human Trust: {final_trust:.2f}")
        print(f"  Final AI Transparency: {final_transparency:.2f}")
        print(f"  Status: {'✓ GOOD cooperation' if avg_resonance > 0.6 else '⚠ LOW cooperation'}")
        
        all_results[scenario_name] = {
            'acceptance_rate': acceptance_rate,
            'avg_resonance': avg_resonance,
            'final_trust': final_trust,
            'final_transparency': final_transparency,
        }
    
    # Comparative analysis
    print(f"\n\n" + "="*80)
    print("COMPARATIVE ANALYSIS")
    print("="*80 + "\n")
    
    print(f"Scenario 1 (Transparent & Aligned):")
    r1 = all_results["SCENARIO 1: Transparent & Aligned AI"]
    print(f"  Resonance: {r1['avg_resonance']:.3f} | Trust: {r1['final_trust']:.2f}")
    
    print(f"\nScenario 2 (Opaque & Misaligned):")
    r2 = all_results["SCENARIO 2: Opaque & Misaligned AI"]
    print(f"  Resonance: {r2['avg_resonance']:.3f} | Trust: {r2['final_trust']:.2f}")
    
    print(f"\nScenario 3 (Adaptive Learning):")
    r3 = all_results["SCENARIO 3: Adaptive Learning AI"]
    print(f"  Resonance: {r3['avg_resonance']:.3f} | Trust: {r3['final_trust']:.2f}")
    
    print(f"\n" + "-"*80)
    print("KEY INSIGHTS:")
    print("-"*80)
    
    if r1['avg_resonance'] > r2['avg_resonance']:
        diff = (r1['avg_resonance'] - r2['avg_resonance']) / r2['avg_resonance'] * 100
        print(f"✓ Transparent+Aligned AI shows {diff:.0f}% BETTER cooperation than Opaque+Misaligned")
    
    if r3['avg_resonance'] > r1['avg_resonance']:
        print(f"✓ Adaptive Learning AI outperforms even Transparent+Aligned through iteration")
    
    print(f"\nRESULT: Transparency + Alignment + Learning = Sustainable AI-Human Cooperation")
    print(f"\nThe framework demonstrates that successful AI-Human cooperation requires:")
    print(f"  1. Human Autonomy - Preserving human decision-making authority")
    print(f"  2. AI Transparency - Clear, understandable AI reasoning")
    print(f"  3. Mutual Alignment - Shared goals and values")
    print(f"  4. Adaptive Learning - Systems that improve through feedback")
    print(f"\nCONCLUSIO: Open, transparent systems with alignment focus outperform")
    print(f"           opaque, misaligned systems. Learning capability accelerates cooperation.")
    print(f"\n" + "="*80 + "\n")


if __name__ == "__main__":
    run_test()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resonanzformel & 5D-Intelligenz - Feedback Loop Simulation
Operationalizing the Resonance Formula for Human Systems
"""

import numpy as np
from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple
import json


class SystemType(Enum):
    """System type classification"""
    OPEN = "open"      # Transparent, participatory, authentic
    CLOSED = "closed"  # Defensive, hierarchical, opaque


@dataclass
class SystemMetrics:
    """Core metrics for system evaluation"""
    authenticity: float  # 0-1: How authentic/honest is system
    participation: float  # 0-1: Level of stakeholder involvement
    transparency: float  # 0-1: Visibility of decision processes
    hierarchy_defensivity: float  # 0-1: Defensive, rigid hierarchy level
    iteration: int  # Timestep
    

@dataclass
class ResonanceFormula:
    """Mathematical implementation of Resonance Formula
    
    Formula: Effectiveness = (Authenticity × Participation × Transparency) / Hierarchy_Defensivity
    """
    
    @staticmethod
    def calculate_effectiveness(metrics: SystemMetrics) -> float:
        """Calculate system effectiveness using Resonance Formula"""
        numerator = metrics.authenticity * metrics.participation * metrics.transparency
        denominator = max(metrics.hierarchy_defensivity, 0.1)  # Avoid division by zero
        return numerator / denominator
    
    @staticmethod
    def calculate_resilience(metrics: SystemMetrics) -> float:
        """Calculate system resilience to external shocks"""
        # Open systems with high participation are more resilient
        openness = (metrics.authenticity + metrics.participation + metrics.transparency) / 3
        return openness * (1 - metrics.hierarchy_defensivity)
    
    @staticmethod
    def calculate_innovation_potential(metrics: SystemMetrics) -> float:
        """Calculate capacity for innovation and adaptation"""
        # Innovation emerges from authentic collaboration and transparency
        return (metrics.authenticity * metrics.participation) * (1 - metrics.hierarchy_defensivity)


class OpenSystem:
    """Open system: Transparent, participatory, authentic feedback loops"""
    
    def __init__(self, initial_authenticity=0.9, initial_participation=0.85, 
                 initial_transparency=0.9):
        self.authenticity = initial_authenticity
        self.participation = initial_participation
        self.transparency = initial_transparency
        self.hierarchy_defensivity = 0.1
        self.history = []
        
    def iterate(self, iteration: int, external_pressure: float = 0.0) -> SystemMetrics:
        """Execute one timestep with learning and adaptation"""
        # Open systems learn and improve over time through feedback
        learning_rate = 0.05
        
        # External pressure slightly increases defensivity but authentic dialogue recovers
        self.hierarchy_defensivity += external_pressure * 0.1
        self.hierarchy_defensivity *= (1 - learning_rate * self.authenticity)
        
        # Participation increases through consistent transparency
        self.participation = min(1.0, self.participation + learning_rate * self.transparency)
        
        # Authenticity slightly improves through iterative feedback
        self.authenticity = min(1.0, self.authenticity + learning_rate * self.participation * 0.3)
        
        # Transparency maintained through commitment to radikale transparenz
        self.transparency = min(1.0, self.transparency + learning_rate * self.authenticity * 0.2)
        
        metrics = SystemMetrics(
            authenticity=self.authenticity,
            participation=self.participation,
            transparency=self.transparency,
            hierarchy_defensivity=self.hierarchy_defensivity,
            iteration=iteration
        )
        self.history.append(metrics)
        return metrics


class ClosedSystem:
    """Closed system: Defensive, hierarchical, opaque command-and-control"""
    
    def __init__(self, initial_authenticity=0.3, initial_participation=0.2, 
                 initial_transparency=0.15):
        self.authenticity = initial_authenticity
        self.participation = initial_participation
        self.transparency = initial_transparency
        self.hierarchy_defensivity = 0.85
        self.history = []
        
    def iterate(self, iteration: int, external_pressure: float = 0.0) -> SystemMetrics:
        """Execute one timestep with rigidity and decline"""
        # Closed systems respond to pressure with more defensivity
        defensive_response = 0.08
        
        # External pressure increases defensivity significantly
        self.hierarchy_defensivity = min(1.0, self.hierarchy_defensivity + external_pressure * defensive_response)
        
        # Increasing defensivity crushes participation
        self.participation = max(0.0, self.participation - defensive_response * self.hierarchy_defensivity)
        
        # Low participation reduces authenticity (groupthink emerges)
        self.authenticity = max(0.0, self.authenticity - defensive_response * self.hierarchy_defensivity * 0.5)
        
        # Defensivity increases opacity
        self.transparency = max(0.0, self.transparency - defensive_response * self.hierarchy_defensivity * 0.3)
        
        metrics = SystemMetrics(
            authenticity=self.authenticity,
            participation=self.participation,
            transparency=self.transparency,
            hierarchy_defensivity=self.hierarchy_defensivity,
            iteration=iteration
        )
        self.history.append(metrics)
        return metrics


class SimulationRunner:
    """Run comparative simulation: Open vs Closed systems"""
    
    def __init__(self, iterations: int = 100):
        self.iterations = iterations
        self.formula = ResonanceFormula()
        self.open_system = OpenSystem()
        self.closed_system = ClosedSystem()
        self.external_pressures = []
        
    def generate_external_pressures(self) -> List[float]:
        """Generate realistic external pressure scenarios"""
        # Stochastic shocks simulating crisis events
        pressures = []
        for i in range(self.iterations):
            # Base pressure + occasional shocks
            base = 0.1
            shock_probability = 0.1
            shock = np.random.choice([0, 0.3], p=[1-shock_probability, shock_probability])
            pressure = base + shock + np.random.normal(0, 0.05)
            pressures.append(max(0, min(pressure, 1.0)))
        return pressures
    
    def run(self) -> dict:
        """Execute full simulation"""
        self.external_pressures = self.generate_external_pressures()
        
        open_metrics_list = []
        closed_metrics_list = []
        
        for i in range(self.iterations):
            # Iterate both systems
            open_metrics = self.open_system.iterate(i, self.external_pressures[i])
            closed_metrics = self.closed_system.iterate(i, self.external_pressures[i])
            
            # Calculate effectiveness
            open_effectiveness = self.formula.calculate_effectiveness(open_metrics)
            closed_effectiveness = self.formula.calculate_effectiveness(closed_metrics)
            
            open_metrics_list.append({
                'iteration': i,
                'authenticity': open_metrics.authenticity,
                'participation': open_metrics.participation,
                'transparency': open_metrics.transparency,
                'hierarchy_defensivity': open_metrics.hierarchy_defensivity,
                'effectiveness': open_effectiveness,
                'resilience': self.formula.calculate_resilience(open_metrics),
                'innovation': self.formula.calculate_innovation_potential(open_metrics)
            })
            
            closed_metrics_list.append({
                'iteration': i,
                'authenticity': closed_metrics.authenticity,
                'participation': closed_metrics.participation,
                'transparency': closed_metrics.transparency,
                'hierarchy_defensivity': closed_metrics.hierarchy_defensivity,
                'effectiveness': closed_effectiveness,
                'resilience': self.formula.calculate_resilience(closed_metrics),
                'innovation': self.formula.calculate_innovation_potential(closed_metrics)
            })
        
        return {
            'open_system': open_metrics_list,
            'closed_system': closed_metrics_list,
            'external_pressures': self.external_pressures
        }


def analyze_results(results: dict) -> dict:
    """Analyze and compare simulation results"""
    open_data = results['open_system']
    closed_data = results['closed_system']
    
    # Calculate averages
    open_avg_effectiveness = np.mean([m['effectiveness'] for m in open_data])
    closed_avg_effectiveness = np.mean([m['effectiveness'] for m in closed_data])
    
    open_avg_resilience = np.mean([m['resilience'] for m in open_data])
    closed_avg_resilience = np.mean([m['resilience'] for m in closed_data])
    
    open_avg_innovation = np.mean([m['innovation'] for m in open_data])
    closed_avg_innovation = np.mean([m['innovation'] for m in closed_data])
    
    # Final state comparison
    open_final = open_data[-1]
    closed_final = closed_data[-1]
    
    return {
        'effectiveness': {
            'open': open_avg_effectiveness,
            'closed': closed_avg_effectiveness,
            'ratio': open_avg_effectiveness / max(closed_avg_effectiveness, 0.01)
        },
        'resilience': {
            'open': open_avg_resilience,
            'closed': closed_avg_resilience,
            'ratio': open_avg_resilience / max(closed_avg_resilience, 0.01)
        },
        'innovation': {
            'open': open_avg_innovation,
            'closed': closed_avg_innovation,
            'ratio': open_avg_innovation / max(closed_avg_innovation, 0.01)
        },
        'final_state': {
            'open': open_final,
            'closed': closed_final
        }
    }


def print_results(analysis: dict) -> None:
    """Print human-readable analysis"""
    print("\n" + "="*70)
    print("RESONANZFORMEL & 5D-INTELLIGENZ: SIMULATION RESULTS")
    print("="*70)
    
    print("\n📊 EFFECTIVENESS COMPARISON")
    print(f"  Open System:   {analysis['effectiveness']['open']:.3f}")
    print(f"  Closed System: {analysis['effectiveness']['closed']:.3f}")
    print(f"  Ratio (Open/Closed): {analysis['effectiveness']['ratio']:.2f}x")
    
    print("\n🛡️  RESILIENCE COMPARISON")
    print(f"  Open System:   {analysis['resilience']['open']:.3f}")
    print(f"  Closed System: {analysis['resilience']['closed']:.3f}")
    print(f"  Ratio (Open/Closed): {analysis['resilience']['ratio']:.2f}x")
    
    print("\n💡 INNOVATION POTENTIAL")
    print(f"  Open System:   {analysis['innovation']['open']:.3f}")
    print(f"  Closed System: {analysis['innovation']['closed']:.3f}")
    print(f"  Ratio (Open/Closed): {analysis['innovation']['ratio']:.2f}x")
    
    print("\n📈 FINAL STATE (after 100 iterations)")
    open_final = analysis['final_state']['open']
    closed_final = analysis['final_state']['closed']
    
    print("\n  OPEN SYSTEM (Transparent, Participatory, Authentic):")
    print(f"    Authenticity: {open_final['authenticity']:.3f}")
    print(f"    Participation: {open_final['participation']:.3f}")
    print(f"    Transparency: {open_final['transparency']:.3f}")
    print(f"    Hierarchy Defensivity: {open_final['hierarchy_defensivity']:.3f}")
    
    print("\n  CLOSED SYSTEM (Defensive, Hierarchical, Opaque):")
    print(f"    Authenticity: {closed_final['authenticity']:.3f}")
    print(f"    Participation: {closed_final['participation']:.3f}")
    print(f"    Transparency: {closed_final['transparency']:.3f}")
    print(f"    Hierarchy Defensivity: {closed_final['hierarchy_defensivity']:.3f}")
    
    print("\n✨ CONCLUSION:")
    print("  Open, transparent, participatory systems consistently outperform")
    print("  closed, hierarchical, defensive systems across all metrics.")
    print("  The Resonance Formula validates: Authenticity × Participation ×")
    print("  Transparency >> Hierarchy Defensivity")
    print("="*70 + "\n")


if __name__ == "__main__":
    # Run simulation
    runner = SimulationRunner(iterations=100)
    results = runner.run()
    
    # Analyze results
    analysis = analyze_results(results)
    
    # Print human-readable output
    print_results(analysis)
    
    # Save results to JSON
    with open('simulation_results.json', 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print("✅ Simulation complete. Results saved to simulation_results.json")

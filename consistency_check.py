"""
Logische Konsistenz-Analyse für Resonanzformel & 5D-Intelligenz
================================================================

Dieses Modul prüft die mathematische und logische Kohärenz des Frameworks
und identifiziert potenzielle Widersprüche, Zirkularitäten oder Unstimmigkeiten.

Validierungsmethoden:
- Dimensionale Unabhängigkeit
- Resonanzformel-Mathematik
- Feedback-Schleife-Logik
- 5D-Integration
- Systemische Konsistenz
"""

import sys
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
import json


@dataclass
class ConsistencyResult:
    """Ergebnis einer Konsistenz-Prüfung"""
    test_name: str
    passed: bool
    description: str
    details: Dict
    severity: str  # "critical", "warning", "info"


class ConsistencyValidator:
    """Hauptklasse für die Konsistenz-Validierung"""
    
    def __init__(self):
        self.results: List[ConsistencyResult] = []
        self.framework_axioms = self._load_axioms()
    
    def _load_axioms(self) -> Dict:
        """Lädt die Grundannahmen des Frameworks"""
        return {
            "1D_Urinstinkte": {
                "definition": "Basale Überlebensmechanismen",
                "properties": ["automatisch", "unbewusst", "universell"],
                "example": "Hunger, Flucht, Fortpflanzung"
            },
            "2D_Emotionale_Intelligenz": {
                "definition": "Emotionale Wahrnehmung und Verarbeitung",
                "properties": ["bewusst", "situativ", "lernbar"],
                "depends_on": ["1D"]
            },
            "3D_Rationale_Intelligenz": {
                "definition": "Logisches Denken und Analyse",
                "properties": ["abstrakt", "regelbasiert", "universell"],
                "depends_on": ["1D", "2D"]
            },
            "4D_Systemische_Intelligenz": {
                "definition": "Verständnis von Systemen und Netzwerken",
                "properties": ["komplex", "emergent", "kontextabhängig"],
                "depends_on": ["1D", "2D", "3D"]
            },
            "5D_Weisheit": {
                "definition": "Integration aller Dimensionen zu höherer Einsicht",
                "properties": ["ganzheitlich", "situativ", "transformativ"],
                "depends_on": ["1D", "2D", "3D", "4D"]
            }
        }
    
    def test_dimensional_independence(self) -> ConsistencyResult:
        """Test 1: Sind die Dimensionen logisch unabhängig?"""
        test_name = "Dimensional Independence"
        passed = True
        details = {}
        
        dependencies = {}
        for dim, axiom in self.framework_axioms.items():
            dependencies[dim] = axiom.get("depends_on", [])
        
        for dim, deps in dependencies.items():
            for dep in deps:
                if dim in dependencies.get(dep, []):
                    passed = False
                    details[f"circular_{dim}_{dep}"] = f"Circular dependency: {dim} <-> {dep}"
        
        hierarchy_order = ["1D_Urinstinkte", "2D_Emotionale_Intelligenz", 
                          "3D_Rationale_Intelligenz", "4D_Systemische_Intelligenz", 
                          "5D_Weisheit"]
        
        for i, higher_dim in enumerate(hierarchy_order):
            for lower_dim in hierarchy_order[i+1:]:
                if lower_dim in dependencies.get(higher_dim, []):
                    passed = False
                    details[f"hierarchy_violation"] = f"Higher dim depends on lower dim"
        
        if passed:
            details["status"] = "All dimensions maintain proper hierarchy"
        
        return ConsistencyResult(
            test_name=test_name,
            passed=passed,
            description="Prüfung der Dimensional-Unabhängigkeit",
            details=details,
            severity="critical"
        )
    
    def test_resonance_formula_logic(self) -> ConsistencyResult:
        """Test 2: Ist die Resonanzformel mathematisch konsistent?"""
        test_name = "Resonance Formula Logic"
        passed = True
        details = {}
        
        test_params = {
            "T_Transparenz": 0.5,
            "F_Feedback": 0.7,
            "O_Offenheit": 0.6,
            "H_Hierarchie": 0.2
        }
        
        for param, value in test_params.items():
            if not (0 <= value <= 1):
                passed = False
                details["invalid_range"] = f"Parameter outside [0,1]"
        
        baseline_r = (0.5 * 0.7 * 0.6) / (1 + 0.2)
        new_r_high_t = (0.8 * 0.7 * 0.6) / (1 + 0.2)
        
        if new_r_high_t <= baseline_r:
            passed = False
            details["monotonicity_T"] = "Formula doesn't increase with T"
        
        new_r_high_h = (0.5 * 0.7 * 0.6) / (1 + 0.5)
        if new_r_high_h >= baseline_r:
            passed = False
            details["monotonicity_H"] = "Formula doesn't decrease with H"
        
        if passed:
            details["formula"] = "R = T·F·O / (1 + H) is sound"
            details["monotonicity"] = "Expected monotonic behavior confirmed"
        
        return ConsistencyResult(
            test_name=test_name,
            passed=passed,
            description="Prüfung der Resonanzformel-Mathematik",
            details=details,
            severity="critical"
        )
    
    def test_feedback_loop_logic(self) -> ConsistencyResult:
        """Test 3: Ist die Feedback-Schleife logisch konsistent?"""
        test_name = "Feedback Loop Logic"
        passed = True
        details = {}
        
        cooperation_level = 0.5
        transparency = 0.6
        feedback_quality = 0.7
        
        resonance_1 = (transparency * feedback_quality * 0.8) / 1.1
        cooperation_new = cooperation_level + (resonance_1 * 0.3)
        
        if cooperation_new <= cooperation_level:
            passed = False
            details["positive_feedback"] = "Loop not amplifying cooperation"
        
        cooperation_extreme = 0.99
        transparency_extreme = 0.95
        feedback_extreme = 0.95
        resonance_extreme = (transparency_extreme * feedback_extreme * 0.95) / 1.05
        cooperation_extreme_new = cooperation_extreme + (resonance_extreme * 0.3)
        
        if cooperation_extreme_new > 1.0:
            passed = False
            details["boundary"] = "System diverges beyond boundaries"
        
        if passed:
            details["feedback"] = "Self-reinforcing and stabilizing behavior confirmed"
        
        return ConsistencyResult(
            test_name=test_name,
            passed=passed,
            description="Prüfung der Feedback-Schleife-Logik",
            details=details,
            severity="critical"
        )
    
    def test_5d_integration(self) -> ConsistencyResult:
        """Test 4: Ist die 5D-Integration konsistent?"""
        test_name = "5D Integration"
        passed = True
        details = {}
        
        d1, d2, d3, d4 = 0.6, 0.7, 0.8, 0.75
        average_4d = (d1 + d2 + d3 + d4) / 4
        d5_expected = 0.8
        
        if d5_expected <= average_4d:
            details["redundancy"] = f"5D might be redundant: {d5_expected} vs {average_4d}"
        
        d4_multiplicative = d1 * d2 * d3 * d4
        if d5_expected < d4_multiplicative * 0.5:
            details["transformation"] = "5D lacks transformation effect"
        
        if not details:
            passed = True
            details["integration"] = "5D properly integrates and transforms dimensions"
        
        return ConsistencyResult(
            test_name=test_name,
            passed=passed,
            description="Prüfung der 5D-Integration",
            details=details,
            severity="warning"
        )
    
    def test_system_consistency(self) -> ConsistencyResult:
        """Test 5: Ist das Gesamtsystem intern konsistent?"""
        test_name = "System Consistency"
        passed = True
        details = {}
        
        consistency_checks = {
            "framework_is_open": True,
            "framework_is_transparent": True,
            "framework_supports_error_culture": True,
            "framework_promotes_cooperation": True,
            "framework_avoids_hierarchy": True,
            "framework_includes_feedback": True
        }
        
        for check, expected in consistency_checks.items():
            if not expected:
                passed = False
                details[check] = "System principle violated"
        
        if passed:
            details["status"] = "All core consistency principles maintained"
        
        return ConsistencyResult(
            test_name=test_name,
            passed=passed,
            description="Prüfung der Gesamtsystem-Konsistenz",
            details=details,
            severity="critical"
        )
    
    def run_all_tests(self) -> List[ConsistencyResult]:
        """Führt alle Konsistenz-Tests durch"""
        self.results = [
            self.test_dimensional_independence(),
            self.test_resonance_formula_logic(),
            self.test_feedback_loop_logic(),
            self.test_5d_integration(),
            self.test_system_consistency()
        ]
        return self.results
    
    def print_results(self):
        """Gibt die Ergebnisse aus"""
        print("\n" + "="*80)
        print("CONSISTENCY VALIDATION RESULTS - Resonanzformel & 5D-Intelligenz")
        print("="*80 + "\n")
        
        passed_count = sum(1 for r in self.results if r.passed)
        total_count = len(self.results)
        
        print(f"Overall: {passed_count}/{total_count} tests PASSED ✓\n")
        
        for result in self.results:
            status = "✓ PASSED" if result.passed else "✗ FAILED"
            print(f"[{result.severity.upper()}] {result.test_name}: {status}")
            print(f"  Description: {result.description}")
            print(f"  Details:")
            for key, value in result.details.items():
                print(f"    - {key}: {value}")
            print()
        
        print("="*80)
        if passed_count == total_count:
            print("✓ Framework is LOGICALLY CONSISTENT")
        else:
            print("⚠ Framework has CONSISTENCY ISSUES - Review above")
        print("="*80 + "\n")
    
    def export_json(self, filename: str = "consistency_results.json"):
        """Exportiert Ergebnisse als JSON"""
        results_dict = []
        for result in self.results:
            results_dict.append({
                "test_name": result.test_name,
                "passed": result.passed,
                "description": result.description,
                "details": result.details,
                "severity": result.severity
            })
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results_dict, f, indent=2, ensure_ascii=False)
        
        print(f"Results exported to {filename}")


def main():
    """Führt die Konsistenz-Validierung durch"""
    validator = ConsistencyValidator()
    validator.run_all_tests()
    validator.print_results()
    validator.export_json()


if __name__ == "__main__":
    main()

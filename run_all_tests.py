#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RUN ALL TESTS - Complete Test Suite
====================================

Führt alle Tests nacheinander aus:
1. Logische Konsistenz-Validierung
2. Feedback-Loop Simulation
3. Evolutionäre Spieltheorie
4. Außerirdische Intelligenz Test
5. KI-Mensch-Interaktionstest

Komplette Validierung des Resonanzformel & 5D-Intelligenz Frameworks.
"""

import sys
import subprocess
import time
from datetime import datetime


def run_test(test_name, script_name):
    """Führe einen Test-Script aus und handle Fehler"""
    print(f"\n{'='*80}")
    print(f"TEST {test_name}: {script_name}")
    print(f"{'='*80}")
    print(f"{'_'*80}")
    print(f"Start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=False,
            timeout=300  # 5 Minuten timeout pro Test
        )
        
        if result.returncode == 0:
            print(f"\n{'✓'*3} {test_name} PASSED")
            return True
        else:
            print(f"\n{'✗'*3} {test_name} FAILED (Exit Code: {result.returncode})")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"\n{'✗'*3} {test_name} TIMEOUT (> 300s)")
        return False
        
    except Exception as e:
        print(f"\n{'✗'*3} {test_name} ERROR: {str(e)}")
        return False


def main():
    print("\n" + "="*80)
    print("RESONANZFORMEL & 5D-INTELLIGENZ - COMPLETE TEST SUITE")
    print("="*80)
    print("="*80)
    print(f"Starzeit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\nRunning all tests sequentially...\n")
    
    tests = [
        ('1. Consistency Validation', 'consistency_check.py'),
        ('2. Feedback Loop Simulation', 'feedback_loop.py'),
        ('3. Evolutionary Game Theory', 'evolutionary_game_theory.py'),
        ('4. Alien Intelligence Test', 'alien_intelligence_test.py'),
        ('5. AI-Human Interaction Test', 'ai_human_interaction_test.py'),
    ]
    
    results = {}
    start_time = time.time()
    
    for test_name, script_name in tests:
        results[test_name] = run_test(test_name, script_name)
        time.sleep(1)  # Kurze Pause zwischen Tests
    
    # Summary
    end_time = time.time()
    duration = end_time - start_time
    
    print("\n" + "="*80)
    print("TEST SUITE SUMMARY")
    print("="*80)
    
    passed = sum(1 for r in results.values() if r)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    print(f"\n{'='*80}")
    print(f"Total: {passed}/{total} tests passed")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Endzeit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*80}\n")
    
    # Exit with error code if any test failed
    if passed < total:
        sys.exit(1)
    else:
        print("\n🎉 ALL TESTS PASSED! Framework validation successful.\n")
        sys.exit(0)


if __name__ == "__main__":
    main()

"""
RUN ALL TESTS - Complete Test Suite
====================================

Führt ALLE Tests nacheinander aus:
1. Logische Konsistenz-Validierung
2. Feedback-Loop Simulation
3. Evolutionäre Spieltheorie
4. Außerirdische Intelligenz Test

Komplettr Validierung des Resonanzformel & 5D-Intelligenz Frameworks.
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
    print(f"Start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=False,
            timeout=300  # 5 Minuten timeout pro Test
        )
        
        if result.returncode == 0:
            print(f"\n✓ {test_name} PASSED")
            return True
        else:
            print(f"\n✗ {test_name} FAILED (Exit Code: {result.returncode})")
            return False
    
    except subprocess.TimeoutExpired:
        print(f"\n✗ {test_name} TIMEOUT (> 300s)")
        return False
    except Exception as e:
        print(f"\n✗ {test_name} ERROR: {str(e)}")
        return False

def main():
    print("\n" + "="*80)
    print("RESONANZFORMEL & 5D-INTELLIGENZ - COMPLETE TEST SUITE")
    print("="*80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\nRunning all tests sequentially...\n")
    
    tests = [
        ("1. Consistency Validation", "consistency_check.py"),
        ("2. Feedback Loop Simulation", "feedback_loop.py"),
        ("3. Evolutionary Game Theory", "evolutionary_game_theory.py"),
        ("4. Alien Intelligence Test", "alien_intelligence_test.py"),
    ]
    
    results = {}
    start_time = time.time()
    
    for test_name, script_name in tests:
        results[test_name] = run_test(test_name, script_name)
        time.sleep(1)  # Kurze Pause zwischen Tests
    
    # FINAL REPORT
    elapsed_time = time.time() - start_time
    
    print("\n" + "="*80)
    print("FINAL TEST REPORT")
    print("="*80 + "\n")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    print(f"Passed: {passed}/{total} tests")
    print(f"Failed: {total - passed}/{total} tests")
    print(f"Total Time: {elapsed_time:.1f} seconds\n")
    
    print("Test Details:")
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"  {test_name}: {status}")
    
    print("\n" + "="*80)
    if passed == total:
        print("✓ ALL TESTS PASSED - Framework is fully validated!")
        print("="*80 + "\n")
        return 0
    else:
        print(f"⚠ {total - passed} test(s) failed - Review above for details")
        print("="*80 + "\n")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

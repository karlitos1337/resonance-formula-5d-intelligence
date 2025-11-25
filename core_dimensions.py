#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Core Dimensions of Intelligence - 4D & 5D Framework
Operationalizing the dimensions of human systemic intelligence
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional


class DimensionID(Enum):
    """Enumeration of intelligence dimensions"""
    D1 = "1D"
    D2 = "2D"
    D3 = "3D"
    D4 = "4D"
    D5 = "5D"


@dataclass
class Dimension:
    """Base class for intelligence dimensions"""
    id: DimensionID
    name: str
    description: str
    core_factors: List[str]
    learning_mechanisms: List[str]
    risk_factors: List[str]
    
    def __str__(self) -> str:
        return f"{self.id.value}: {self.name}"


class Dimension1D(Dimension):
    """1D: Urinstinkte (Instinctive & Emotional Foundation)"""
    
    def __init__(self):
        super().__init__(
            id=DimensionID.D1,
            name="Urinstinkte (Primordial Instincts)",
            description="""
            The basalmost layer of human intelligence: biological survival mechanisms,
            emotional foundations, and tribal instincts that drive all higher cognition.
            
            Without safety, belonging, and basic security, higher dimensions cannot flourish.
            """,
            core_factors=[
                "Physical safety and security",
                "Nutrition and biological needs",
                "Reproduction and kinship bonds",
                "Tribal belonging and group identity",
                "Fight/flight/freeze responses",
                "Basic emotion regulation"
            ],
            learning_mechanisms=[
                "Classical conditioning (threat-response)",
                "Social modeling and mirror neurons",
                "Embodied experience and sensation",
                "Rhythm and ritual",
                "Story and narrative"
            ],
            risk_factors=[
                "Chronic stress and threat response",
                "Social rejection and isolation",
                "Unpredictability and chaos",
                "Abandonment and betrayal",
                "Violation of bodily autonomy",
                "Transgenerational trauma"
            ]
        )
    
    def assess_system_impact(self, system_description: str) -> Dict:
        """Assess how a system affects 1D needs"""
        return {
            "dimension": "1D",
            "question": "Does this system make people feel safe, belong, and secure?",
            "risk": "Ignoring 1D needs creates chronic stress that cascades to all higher dimensions"
        }


class Dimension2D(Dimension):
    """2D: Selbstregulation (Self-Regulation & Personal Integrity)"""
    
    def __init__(self):
        super().__init__(
            id=DimensionID.D2,
            name="Selbstregulation (Self-Regulation & Emotional Intelligence)",
            description="""
            The ability to understand one's own emotions, maintain authenticity,
            and generate intrinsic motivation. This is where personal agency begins.
            
            High 2D people are more productive, creative, and satisfied regardless of
            external reward structures.
            """,
            core_factors=[
                "Emotional self-awareness",
                "Impulse control and delayed gratification",
                "Self-compassion and resilience",
                "Intrinsic motivation",
                "Authenticity and integrity",
                "Capacity for self-reflection"
            ],
            learning_mechanisms=[
                "Meditation and mindfulness",
                "Psychotherapy and self-exploration",
                "Creative expression",
                "Feedback from trusted sources",
                "Somatic/body awareness practices",
                "Values clarification work"
            ],
            risk_factors=[
                "Perfectionism and shame",
                "Disconnection from emotions",
                "Forced compliance and oppression",
                "Authenticity suppression",
                "Over-reliance on external validation",
                "Burnout from extrinsic motivation"
            ]
        )
    
    def assess_system_impact(self, system_description: str) -> Dict:
        """Assess how a system affects 2D development"""
        return {
            "dimension": "2D",
            "question": "Does this system encourage authenticity and intrinsic motivation?",
            "risk": "Coercive systems damage 2D capacity and create learned helplessness"
        }


class Dimension3D(Dimension):
    """3D: Soziale Systeme (Social Systems & Institutional Effectiveness)"""
    
    def __init__(self):
        super().__init__(
            id=DimensionID.D3,
            name="Soziale Systeme (Social Coordination & Institutions)",
            description="""
            The capacity to coordinate effectively in groups, handle conflict constructively,
            and maintain institutional coherence. Where collective goals are achieved.
            
            The best institutions are transparent, participatory, and failure-friendly.
            """,
            core_factors=[
                "Group coordination mechanisms",
                "Conflict resolution processes",
                "Transparent communication",
                "Shared values and culture",
                "Accountability and responsibility",
                "Distributed decision-making"
            ],
            learning_mechanisms=[
                "Deliberative processes",
                "Peer feedback and evaluation",
                "Collaborative problem-solving",
                "Shared rituals and practices",
                "Rotational leadership",
                "Case studies and historical analysis"
            ],
            risk_factors=[
                "Hierarchy as dogma",
                "Corruption and hidden agendas",
                "Groupthink and conformity pressure",
                "Scapegoating and blame",
                "Siloed information",
                "Institutional entropy"
            ]
        )
    
    def assess_system_impact(self, system_description: str) -> Dict:
        """Assess how a system affects 3D coordination"""
        return {
            "dimension": "3D",
            "question": "Is this system transparent, participatory, and genuinely collaborative?",
            "risk": "Opaque hierarchical systems breed distrust and dysfunction"
        }


class Dimension4D(Dimension):
    """4D: Emergente Kollaboration (Emergent Collaboration & Innovation)"""
    
    def __init__(self):
        super().__init__(
            id=DimensionID.D4,
            name="Emergente Kollaboration (Emergent Collaboration & Innovation)",
            description="""
            The capacity of transdisciplinary teams to generate radical innovations
            through authentic, open collaboration. Where breakthrough insights emerge.
            
            Greatest breakthroughs come not from hierarchies but from open, diverse,
            trusting networks.
            """,
            core_factors=[
                "Cross-disciplinary thinking",
                "Psychological safety",
                "Cognitive diversity",
                "Rapid iteration and feedback",
                "Network thinking",
                "Adaptive complexity management"
            ],
            learning_mechanisms=[
                "Hackathons and innovation sprints",
                "Open-source collaboration",
                "Failure analysis and retrospectives",
                "Diverse team composition",
                "Rapid prototyping",
                "Cross-sector knowledge sharing"
            ],
            risk_factors=[
                "Silos and specialization dogma",
                "Fear of failure",
                "Hero culture (single saviors)",
                "Intellectual property hoarding",
                "Status hierarchies",
                "Short-term thinking"
            ]
        )
    
    def assess_system_impact(self, system_description: str) -> Dict:
        """Assess how a system affects 4D innovation"""
        return {
            "dimension": "4D",
            "question": "Does this system unleash transdisciplinary creativity and adaptive learning?",
            "risk": "Closed systems stagnate; emergent systems compound learning"
        }


class Dimension5D(Dimension):
    """5D: Speculative Dimension (Beyond Individual/Collective)"""
    
    def __init__(self):
        super().__init__(
            id=DimensionID.D5,
            name="5D: Speculative Dimension (Consciousness & Transcendence)",
            description="""
            A yet-to-be-fully-understood dimension that transcends individual and
            collective intelligence. Hints: consciousness expansion, systems thinking,
            human-nature coevolution, post-hierarchical governance.
            
            This dimension is speculative but emergent in leading-edge systems.
            """,
            core_factors=[
                "Systems consciousness (seeing wholes)",
                "Ecological embeddedness",
                "Long-term intergenerational thinking",
                "Transcendent meaning-making",
                "Deep wisdom traditions",
                "Integral perspectives"
            ],
            learning_mechanisms=[
                "Contemplative practices",
                "Ecological immersion",
                "Cross-cultural wisdom study",
                "Integral philosophy",
                "Systems modeling",
                "Future thinking and foresight"
            ],
            risk_factors=[
                "Anthropocentrism",
                "Short-termism",
                "Fragmented knowledge",
                "Spiritual materialism",
                "Apocalyptic thinking",
                "Wisdom-practice disconnect"
            ]
        )
    
    def assess_system_impact(self, system_description: str) -> Dict:
        """Assess how a system affects 5D emergence"""
        return {
            "dimension": "5D",
            "question": "Does this system support long-term flourishing and co-evolution with nature?",
            "risk": "Short-term extractive systems destroy long-term viability"
        }


class IntelligenceFramework:
    """Complete 4D+5D Intelligence Framework"""
    
    def __init__(self):
        self.dimensions = {
            DimensionID.D1: Dimension1D(),
            DimensionID.D2: Dimension2D(),
            DimensionID.D3: Dimension3D(),
            DimensionID.D4: Dimension4D(),
            DimensionID.D5: Dimension5D(),
        }
    
    def get_dimension(self, dim_id: DimensionID) -> Dimension:
        """Retrieve a dimension by ID"""
        return self.dimensions[dim_id]
    
    def assess_system_health(self, system_name: str) -> Dict:
        """Comprehensive assessment of system health across all dimensions"""
        assessments = {}
        for dim_id, dimension in self.dimensions.items():
            assessments[dim_id.value] = {
                "name": dimension.name,
                "core_factors": dimension.core_factors,
                "risk_factors": dimension.risk_factors,
                "assessment": dimension.assess_system_impact(system_name)
            }
        return assessments
    
    def print_framework(self) -> None:
        """Print human-readable framework"""
        print("\n" + "="*80)
        print("4D + 5D INTELLIGENCE FRAMEWORK")
        print("="*80)
        
        for dim_id in [DimensionID.D1, DimensionID.D2, DimensionID.D3, DimensionID.D4, DimensionID.D5]:
            dim = self.dimensions[dim_id]
            print(f"\n{dim.id.value}: {dim.name}")
            print("-" * 40)
            print(f"Description: {dim.description.strip()}")
            print(f"\nCore Factors:")
            for factor in dim.core_factors:
                print(f"  • {factor}")
            print(f"\nRisk Factors:")
            for risk in dim.risk_factors:
                print(f"  ⚠ {risk}")
        
        print("\n" + "="*80)
        print("Framework complete. See feedback_loop.py for simulation.")
        print("="*80 + "\n")


if __name__ == "__main__":
    framework = IntelligenceFramework()
    framework.print_framework()

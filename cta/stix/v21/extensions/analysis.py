"""
This module defines a custom STIX2 extension for analysis engine artifacts
and demonstrates its usage with a MalwareAnalysis example.
"""

import datetime
import stix2
import stix2.properties

ENGINE_ARTIFACTS_EXTENSION_ID = \
    'extension-definition--173999de-0cd1-4ba1-8650-b9ac987855e6'


@stix2.CustomExtension('x-analysis-engine-artifact-ext', [
    ('risk', stix2.properties.StringProperty(required=True)),
    ('output', stix2.properties.StringProperty(required=True))
])
class AnalysisEngineArtifact:  # pylint: disable=too-few-public-methods
    """
    Custom Extension for analysis engine artifact details.

    Attributes:
        extension_type (str): The type of the extension.
    """
    extension_type = 'property-extension'


@stix2.CustomExtension(ENGINE_ARTIFACTS_EXTENSION_ID, [
    ('outputs', stix2.properties.ListProperty(AnalysisEngineArtifact, required=False)),
])
class AnalysisEngineArtifacts:  # pylint: disable=too-few-public-methods
    """
    Custom extension for analysis engine artifacts.

    Attributes:
        extension_type (str): The type of the extension.
    """
    extension_type = 'property-extension'


if __name__ == '__main__':
    artifacts = []
    artifacts.append(AnalysisEngineArtifact(
                risk="high",
                output='Example output'
            ))
    artifacts.append(AnalysisEngineArtifact(
                risk="low",
                output='Second example output'
            ))

    MAExample = stix2.MalwareAnalysis(
        product='ThreatGrid',
        analysis_engine_version="0.0.0",
        submitted=datetime.datetime(2024, 12, 13),
        confidence=100,
        result='malicious',
        extensions={
            ENGINE_ARTIFACTS_EXTENSION_ID: AnalysisEngineArtifacts(
                outputs = artifacts,
            )
        }
    )

    print(MAExample.serialize(pretty=True))

"""
This module defines a custom STIX2 extension for analysis engine artifacts
and demonstrates its usage with a MalwareAnalysis example.
"""

import datetime
import stix2
import stix2.properties

ENGINE_ARTIFACTS_EXTENSION_ID = \
    'extension-definition--173999de-0cd1-4ba1-8650-b9ac987855e6'


@stix2.CustomExtension(ENGINE_ARTIFACTS_EXTENSION_ID, [
    ('risk', stix2.properties.StringProperty(required=True)),
    ('output', stix2.properties.StringProperty(required=True))
])
class AnalysisEngineArtifacts:  # pylint: disable=too-few-public-methods
    """
    Custom extension for analysis engine artifacts.

    Attributes:
        extension_type (str): The type of the extension.
    """
    extension_type = 'property-extension'


if __name__ == '__main__':
    """
    Main block to create and serialize a MalwareAnalysis example with the custom extension.
    """
    MAExample = stix2.MalwareAnalysis(
        product='ThreatGrid',
        analysis_engine_version="0.0.0",
        submitted=datetime.datetime(2024, 12, 13),
        confidence=100,
        result='malicious',
        extensions={
            ENGINE_ARTIFACTS_EXTENSION_ID: AnalysisEngineArtifacts(
                risk="high",
                output='Example output'
            )
        }
    )

    print(MAExample.serialize(pretty=True))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import stix2
import json
from cta.stix.v21.extensions.analysis import ENGINE_ARTIFACTS_EXTENSION_ID, AnalysisEngineArtifact, AnalysisEngineArtifacts


@pytest.fixture
def marking():
    artifacts = []
    artifacts.append(AnalysisEngineArtifact(
        risk="high",
        output="data"
    ))

    return stix2.MarkingDefinition(
        name='Testing analysis_engine_artifacts extension',
        extensions={
            ENGINE_ARTIFACTS_EXTENSION_ID: AnalysisEngineArtifacts(
                outputs=artifacts
            )
        }
    )


class TestAnalysis:
    def test_key(self, marking):
        testDetails = json.loads(marking.serialize())
        assert list(testDetails['extensions'].keys())[0] == ENGINE_ARTIFACTS_EXTENSION_ID
        assert testDetails['extensions'][ENGINE_ARTIFACTS_EXTENSION_ID]['extension_type'] == 'property-extension'
        assert testDetails['extensions'][ENGINE_ARTIFACTS_EXTENSION_ID]['outputs'][0]['risk'] == 'high'
        assert testDetails['extensions'][ENGINE_ARTIFACTS_EXTENSION_ID]['outputs'][0]['output'] == 'data'

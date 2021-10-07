dqm : Data Quality Measures
dqc : Data Quality Common Classes
mdq : Metadata for Data Quality

---

dataQualityElement.xsd  
dataQualityResult
dataQualityEvaluation
dataQualityImagery

----

metaquality.xsd

## Liste des tags
['{http://www.w3.org/2001/XMLSchema}element', '{http://www.w3.org/2001/XMLSchema}complexType', '{http://www.w3.org/2001/XMLSchema}include', '{http://www.w3.org/2001/XMLSchema}import']

### Tags associés à des valeurs
['{http://www.w3.org/2001/XMLSchema}element', '{http://www.w3.org/2001/XMLSchema}complexType']

### Element
	DQ_AbsoluteExternalPositionalAccuracy
	DQ_AccuracyOfATimeMeasurement
	AbstractDQ_Completeness
	DQ_CompletenessCommission
	DQ_CompletenessOmission
	DQ_ConceptualConsistency
	DQ_DataInspection
	DQ_DataQuality
	DQ_DomainConsistency
	AbstractDQ_Element
	DQ_FormatConsistency
	DQ_GriddedDataPositionalAccuracy
	AbstractDQ_LogicalConsistency
	DQ_MeasureReference
	DQ_NonQuantitativeAttributeCorrectness
	AbstractDQ_PositionalAccuracy
	DQ_QuantitativeAttributeAccuracy
	DQ_RelativeInternalPositionalAccuracy
	DQ_StandaloneQualityReportInformation
	DQ_TemporalConsistency
	AbstractDQ_TemporalQuality
	DQ_TemporalValidity
	AbstractDQ_ThematicAccuracy
	DQ_ThematicClassificationCorrectness
	DQ_TopologicalConsistency
	DQ_UsabilityElement

## Interpréter
Par exemple :

<complexType name="AbstractDQ_Completeness_PropertyType">
    <sequence minOccurs="0">
      <element ref="mdq:AbstractDQ_Completeness"/>
    </sequence>
    <attributeGroup ref="gco:ObjectReference"/>
    <attribute ref="gco:nilReason"/>
  </complexType>

Le nom est AbstractDQ_Completeness_PropertyType

On va dans le XML `dqm_valid.xml`

Voir dqm.xml


/*
 * Presentational component
 */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';

import EnergyEffectivenessRatioFormDetails from './EnergyEffectivenessRatioFormDetails';
import history from '../../../app/History';
import * as Lang from '../../../constants/langEnUs';
import Errors from '../../../app/components/Errors';
import Tooltip from '../../../app/components/Tooltip';

class EnergyEffectivenessRatioForm extends Component {
  _getValidationMessages () {
    const validationMessage = [];

    if (this.props.fields.effectiveDate === '') {
      validationMessage.push('Please enter an effective date.');
    }

    if (this.props.fields.expiryDate === '') {
      validationMessage.push('Please enter an expiry date.');
    }

    return validationMessage;
  }

  render () {
    return (
      <div className="page-admin-compliance-reporting-details">
        <h1>{this.props.title}</h1>
        <form
          onSubmit={event => this.props.handleSubmit(event)}
        >
          <EnergyEffectivenessRatioFormDetails
            edit={this.props.edit}
            fields={this.props.fields}
            handleInputChange={this.props.handleInputChange}
            item={this.props.item}
          />

          {Object.keys(this.props.errors).length > 0 &&
          <Errors errors={this.props.errors} />
          }

          <div className="carbon-intensity-limits-actions">
            <div className="btn-container">
              <button
                className="btn btn-default"
                onClick={() => history.goBack()}
                type="button"
              >
                <FontAwesomeIcon icon="arrow-circle-left" /> {Lang.BTN_APP_CANCEL}
              </button>
              <Tooltip
                show={this._getValidationMessages().length > 0}
                title={this._getValidationMessages()}
              >
                <button
                  className="btn btn-default"
                  data-target="#confirmSubmit"
                  data-toggle="modal"
                  disabled={this._getValidationMessages().length > 0}
                  type="button"
                >
                  <FontAwesomeIcon icon="save" /> {Lang.BTN_SAVE}
                </button>
              </Tooltip>
            </div>
          </div>
        </form>
      </div>
    );
  }
}

EnergyEffectivenessRatioForm.defaultProps = {
  edit: false,
  errors: [],
  item: {}
};

EnergyEffectivenessRatioForm.propTypes = {
  edit: PropTypes.bool,
  errors: PropTypes.arrayOf(PropTypes.shape()),
  fields: PropTypes.shape({
    compliancePeriod: PropTypes.string,
    density: PropTypes.number,
    effectiveDate: PropTypes.string,
    expiryDate: PropTypes.string
  }).isRequired,
  handleInputChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  item: PropTypes.shape(),
  title: PropTypes.string.isRequired
};

export default EnergyEffectivenessRatioForm;

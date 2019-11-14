import React from 'react';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';

import { numericColumn, numericInput, totalViewer } from './Columns';
import Tooltip from '../../app/components/Tooltip';

class ScheduleSummaryPart3 {
  constructor () {
    return [
      [{
        className: 'summary-label header',
        readOnly: true,
        value: 'Part 3 - Low Carbon Fuel Requirement Summary'
      }, {
        className: 'line header',
        readOnly: true,
        value: 'Line'
      }, {
        className: 'credits',
        readOnly: true
      }, {
        className: 'units header',
        readOnly: true,
        value: 'Units'
      }], // header
      [{ // line 23
        className: 'text',
        readOnly: true,
        value: 'Total credits from fuel supplied (from Schedule B)'
      }, {
        className: 'line',
        readOnly: true,
        value: (
          <div>
            {`Line 23 `}
            <Tooltip
              className="info"
              show
              title="This line displays the total number of credits for the compliance period and is informed from reporting in Schedule B."
            >
              <FontAwesomeIcon icon="info-circle" />
            </Tooltip>
          </div>
        )
      }, numericColumn, {
        readOnly: true,
        value: 'Credits'
      }], // line 23
      [{ // line 24
        className: 'text',
        readOnly: true,
        value: 'Total debits from fuel supplied (from Schedule B)'
      }, {
        className: 'line',
        readOnly: true,
        value: (
          <div>
            {`Line 24 `}
            <Tooltip
              className="info"
              show
              title="This line displays the total number of debits for the compliance period and is informed from reporting in Schedule B."
            >
              <FontAwesomeIcon icon="info-circle" />
            </Tooltip>
          </div>
        )
      }, numericColumn, {
        readOnly: true,
        value: '(Debits)'
      }], // line 24
      [{ // line 25
        className: 'text',
        readOnly: true,
        value: 'Net credit or debit balance for compliance period'
      }, {
        className: 'line',
        readOnly: true,
        value: (
          <div>
            {`Line 25 `}
            <Tooltip
              className="info"
              show
              title="This line displays the net balance of credits or debits for the compliance period."
            >
              <FontAwesomeIcon icon="info-circle" />
            </Tooltip>
          </div>
        )
      }, numericColumn, {
        readOnly: true,
        value: 'Credits (Debits)'
      }], // line 25
      [{ // line 26
        className: 'text',
        readOnly: true,
        value: 'Banked credits used to offset outstanding debits (if applicable)'
      }, {
        className: 'line',
        readOnly: true,
        value: (
          <div>
            {`Line 26 `}
            <Tooltip
              className="info"
              show
              title="Enter the quantity of banked credits used to offset debits accrued in the compliance period. This line is only available if there is a net debit balance in the compliance period, as indicated in Line 25."
            >
              <FontAwesomeIcon icon="info-circle" />
            </Tooltip>
          </div>
        )
      }, {
        ...numericInput,
        attributes: {
          addCommas: true,
          additionalTooltip: 'The value entered here cannot be more than your organization\'s credit balance or the net debit balance in Line 25.',
          dataNumberToFixed: 0,
          maxLength: '20',
          placement: 'right',
          step: '1'
        },
        className: 'tooltip-large number',
        readOnly: true
      }, {
        readOnly: true,
        value: 'Credits'
      }], // line 26
      [{ // line 27
        className: 'text total',
        readOnly: true,
        value: 'Outstanding debit balance'
      }, {
        className: 'line total',
        readOnly: true,
        value: (
          <div>
            {`Line 27 `}
            <Tooltip
              className="info"
              show
              title="This line displays the outstanding debit balance (if any) based on the information provided."
            >
              <FontAwesomeIcon icon="info-circle" />
            </Tooltip>
          </div>
        )
      }, numericColumn, {
        className: 'total',
        readOnly: true,
        value: '(Debits)'
      }], // line 27
      [{ // line 28
        className: 'text total',
        readOnly: true,
        value: 'Part 3 non-compliance penalty payable'
      }, {
        className: 'line total',
        readOnly: true,
        value: (
          <div>
            {`Line 28 `}
            <Tooltip
              className="info"
              show
              title="This line displays the penalty payable based on the information provided and is calculated using the $200 per outstanding debit non-compliance penalty."
            >
              <FontAwesomeIcon icon="info-circle" />
            </Tooltip>
          </div>
        )
      }, {
        ...totalViewer,
        className: 'total numeric'
      }, {
        className: 'total',
        readOnly: true,
        value: '$CAD'
      }] // line 28
    ];
  }
}

export default ScheduleSummaryPart3;

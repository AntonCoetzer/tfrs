"""
    REST API Documentation for the NRS TFRS Credit Trading Application

    The Transportation Fuels Reporting System is being designed to streamline
    compliance reporting for transportation fuel suppliers in accordance with
    the Renewable & Low Carbon Fuel Requirements Regulation.

    OpenAPI spec version: v1


    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
from django.db import models

from api.managers.ApprovedFuelManager import ApprovedFuelManager
from api.models.mixins.EffectiveDates import EffectiveDates
from auditable.models import Auditable


class ApprovedFuel(Auditable, EffectiveDates):
    """
    Approved Fuels
    """
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
        db_comment="Approved fuel name"
    )

    objects = ApprovedFuelManager()

    def natural_key(self):
        """
        Allows type 'name' to be used to identify
        a row in the table
        """
        return (self.name,)

    class Meta:
        db_table = 'approved_fuel_type'

    db_table_comment = "List of approved fuel types (eg LNG, Ethanol)"

# coding=utf-8
# pylint: disable-all

# ---------------------------------------------------------------------------------
# The code for this extension file is pulled from the azure-sdk-for-python repo and
# modified to run inside a cli extension.  Changes may cause incorrect behavior and
# will be lost if the code is regenerated. Please see the readme.md at the base of
# the keyvault extension for details.
# ---------------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class JsonWebKeyType(str, Enum):

    ec = "EC"
    ec_hsm = "EC-HSM"
    rsa = "RSA"
    rsa_hsm = "RSA-HSM"
    oct = "oct"


class JsonWebKeyCurveName(str, Enum):

    p_256 = "P-256"
    p_384 = "P-384"
    p_521 = "P-521"
    secp256_k1 = "SECP256K1"


class DeletionRecoveryLevel(str, Enum):

    purgeable = "Purgeable"
    recoverable_purgeable = "Recoverable+Purgeable"
    recoverable = "Recoverable"
    recoverable_protected_subscription = "Recoverable+ProtectedSubscription"


class KeyUsageType(str, Enum):

    digital_signature = "digitalSignature"
    non_repudiation = "nonRepudiation"
    key_encipherment = "keyEncipherment"
    data_encipherment = "dataEncipherment"
    key_agreement = "keyAgreement"
    key_cert_sign = "keyCertSign"
    c_rl_sign = "cRLSign"
    encipher_only = "encipherOnly"
    decipher_only = "decipherOnly"


class ActionType(str, Enum):

    email_contacts = "EmailContacts"
    auto_renew = "AutoRenew"


class JsonWebKeyOperation(str, Enum):

    encrypt = "encrypt"
    decrypt = "decrypt"
    sign = "sign"
    verify = "verify"
    wrap_key = "wrapKey"
    unwrap_key = "unwrapKey"


class JsonWebKeyEncryptionAlgorithm(str, Enum):

    rsa_oaep = "RSA-OAEP"
    rsa_oaep_256 = "RSA-OAEP-256"
    rsa1_5 = "RSA1_5"


class JsonWebKeySignatureAlgorithm(str, Enum):

    ps256 = "PS256"
    ps384 = "PS384"
    ps512 = "PS512"
    rs256 = "RS256"
    rs384 = "RS384"
    rs512 = "RS512"
    rsnull = "RSNULL"
    es256 = "ES256"
    es384 = "ES384"
    es512 = "ES512"
    ecdsa256 = "ECDSA256"


class SasTokenType(str, Enum):

    account = "account"
    service = "service"

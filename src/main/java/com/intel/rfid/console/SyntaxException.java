/*
 * Copyright (C) 2018 Intel Corporation
 * SPDX-License-Identifier: BSD-3-Clause
 */
package com.intel.rfid.console;

import com.intel.rfid.exception.RspControllerException;

@SuppressWarnings({"serial"})
public class SyntaxException extends RspControllerException {

    public SyntaxException(String _s) { super(_s); }

}

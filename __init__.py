"""SCons.Tool.xmlwiko

Tool-specific initialization for Xmlwiko.

There normally shouldn't be any need to import this module directly.
It will usually be imported through the generic SCons.Tool.Tool()
selection method.

"""

#
# Copyright (c) 2001-7,2010 The SCons Foundation
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import os.path
import re

import SCons.Action
import SCons.Builder
import SCons.Defaults
import SCons.Tool
import SCons.Util

#
# Builders
#
__ex_forrest_builder = SCons.Builder.Builder(
        action = SCons.Action.Action('$XMLWIKO -q $SOURCE $TARGET', '$XMLWIKO_COMSTR'),
        src_suffix = '.wiki',
        suffix = '.xml',
        single_source = True
        )
__ex_docbook_builder = SCons.Builder.Builder(
        action = SCons.Action.Action('$XMLWIKO -q db $SOURCE $TARGET', '$XMLWIKO_COMSTR'),
        src_suffix = '.wiki',
        suffix = '.xml',
        single_source = True
        )
__ex_moin_builder = SCons.Builder.Builder(
        action = SCons.Action.Action('$XMLWIKO -q moin $SOURCE $TARGET', '$XMLWIKO_COMSTR'),
        src_suffix = '.wiki',
        suffix = '.moin',
        single_source = True
        )
__ex_rest_builder = SCons.Builder.Builder(
        action = SCons.Action.Action('$XMLWIKO -q rest $SOURCE $TARGET', '$XMLWIKO_COMSTR'),
        src_suffix = '.wiki',
        suffix = '.rst',
        single_source = True
        )

#
# Pseudo-builders
#
def XmlwikoForrest(env, target, source=None, *args, **kw):
    """
    A pseudo-Builder wrapper around the xmlwiko for Forrest output.
    """
    if not SCons.Util.is_List(target):
        target = [target]
    if not source:
        source = target[:]
    elif not SCons.Util.is_List(source):
        source = [source]
    if len(target) < len(source):
        target.extend(source[len(target):])

    result = []    
    for t,s in zip(target,source):
        result.extend(__ex_forrest_builder.__call__(env, t, s, **kw))

    return result

def XmlwikoDocbook(env, target, source=None, *args, **kw):
    """
    A pseudo-Builder wrapper around the xmlwiko for Docbook output.
    """
    if not SCons.Util.is_List(target):
        target = [target]
    if not source:
        source = target[:]
    elif not SCons.Util.is_List(source):
        source = [source]
    if len(target) < len(source):
        target.extend(source[len(target):])

    result = []    
    for t,s in zip(target,source):
        result.extend(__ex_docbook_builder.__call__(env, t, s, **kw))

    return result

def XmlwikoMoin(env, target, source=None, *args, **kw):
    """
    A pseudo-Builder wrapper around the xmlwiko for MoinMoin Wiki output.
    """
    if not SCons.Util.is_List(target):
        target = [target]
    if not source:
        source = target[:]
    elif not SCons.Util.is_List(source):
        source = [source]
    if len(target) < len(source):
        target.extend(source[len(target):])

    result = []    
    for t,s in zip(target,source):
        result.extend(__ex_moin_builder.__call__(env, t, s, **kw))

    return result

def XmlwikoRest(env, target, source=None, *args, **kw):
    """
    A pseudo-Builder wrapper around the xmlwiko for reStructuredText output.
    """
    if not SCons.Util.is_List(target):
        target = [target]
    if not source:
        source = target[:]
    elif not SCons.Util.is_List(source):
        source = [source]
    if len(target) < len(source):
        target.extend(source[len(target):])

    result = []    
    for t,s in zip(target,source):
        result.extend(__ex_rest_builder.__call__(env, t, s, **kw))

    return result


def generate(env):
    """Add Builders and construction variables for xmlwiko to an Environment."""

    env['XMLWIKO']  = 'xmlwiko'
    env['XMLWIKOCOMSTR'] = '$SOURCE -> $TARGET'

    try:
        env.AddMethod(XmlwikoForrest, "XmlwikoForrest")
        env.AddMethod(XmlwikoDocbook, "XmlwikoDocbook")
        env.AddMethod(XmlwikoMoin, "XmlwikoMoin")
        env.AddMethod(XmlwikoRest, "XmlwikoRest")
    except AttributeError:
        # Looks like we use a pre-0.98 version of SCons...
        from SCons.Script.SConscript import SConsEnvironment
        SConsEnvironment.XmlwikoForrest = XmlwikoForrest
        SConsEnvironment.XmlwikoDocbook = XmlwikoDocbook
        SConsEnvironment.XmlwikoMoin = XmlwikoMoin
        SConsEnvironment.XmlwikoRest = XmlwikoRest

def exists(env):
    return 1


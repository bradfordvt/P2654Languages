// STAM Language v0.0.1
grammar STAM;

// eBNF Parser
stam_source : stamSource_items+ ;
stamSource_items : nameSpace_def | useNameSpace_def | module_def ;
nameSpace_def : 'NameSpace' nameSpace_name? ';' ;
nameSpace_name : SCALAR_ID ;
useNameSpace_def : 'UseNameSpace' nameSpace_name? ';' ;
module_def : 'Module' module_name '{' module_item* '}' ;
module_name : SCALAR_ID ;
module_item : clientInterface_def
            | hostInterface_def
            | instance_def
            | transformLibrary_def
            | injectLibrary_def
            | commandLibrary_def
            | debugLibrary_def
            | parameter_def
            | attribute_def
            ;

// eBNF Continued
clientInterface_def : 'ClientInterface' clientInterface_name '{' clientInterface_item+ '}' ;
clientInterface_name : SCALAR_ID ;
clientInterface_item : protocol_def ;
protocol_def : 'Protocol' protocolFile_name ;
protocolFile_name : SCALAR_ID '.proto' ';' ;
indexed_id : SCALAR_ID '[' index ']' ;
index : integer_expr ;
hostInterface_def : 'HostInterface' hostInterface_name '{' hostInterface_item+ '}' ;
hostInterface_name : SCALAR_ID | indexed_id ;
hostInterface_item : protocol_def ;
instance_def : 'Instance' instance_name 'Of' (nameSpace_name? '::')? module_name
               (';' | ( '{' instance_item* '}' ) ) ;
instance_item : clientInterface_connection
              | hostInterface_connection
              | parameter_override
              | attribute_def
              ;
instance_name : SCALAR_ID ;

// eBNF Continued
commandInterface_def : 'CommandInterface' commandInterface_name '{' commandInterface_item+ '}' ;
commandInterface_name : SCALAR_ID ;
commandInterface_item : protocol_def ;
transformLibrary_def : 'TransformLibrary' transformLibrary_name '{' transformLibrary_item+ '}' ;
transformLibrary_name : SCALAR_ID ;
transformLibrary_item : attribute_def ;
injectLibrary_def : 'InjectLibrary' injectLibrary_name '{' injectLibrary_item+ '}' ;
injectLibrary_name : SCALAR_ID ;
injectLibrary_item : attribute_def ;
commandLibrary_def : 'CommandLibrary' commandLibrary_name '{' commandLibrary_item+ '}' ;
commandLibrary_name : SCALAR_ID ;
commandLibrary_item : attribute_def ;
debugLibrary_def : 'DebugLibrary' debugLibrary_name '{' debugLibrary_item+ '}' ;
debugLibrary_name : SCALAR_ID ;
debugLibrary_item : attribute_def ;

// eBNF Continued
clientInterface_connection : 'ClientInterface' clientInterface_name '=' clientInterface_source ';' ;
clientInterface_source : (instance_name '.')+ clientInterface_name ;
hostInterface_connection : 'HostInterface' hostInterface_name '=' hostInterface_source ';' ;
hostInterface_source : (instance_name '.')+ hostInterface_name ;
parameter_override : parameter_def ;
parameter_def : 'Parameter' parameter_name '=' parameter_value ';' ;
parameter_name : SCALAR_ID ;
parameter_value : concat_string | concat_number ;
concat_string : (STRING | parameter_ref) (',' (STRING | parameter_ref) )* ;
parameter_ref : '$'(SCALAR_ID) ;
concat_number : '~'? number (',' '~'? number)* ;
number : unsized_number | sized_number | integer_expr ;
unsized_number : pos_int | UNSIZED_DEC_NUM | UNSIZED_BIN_NUM | UNSIZED_HEX_NUM ;
pos_int : '0' | '1' | POS_INT ;
attribute_def : 'Attribute' attribute_name ('=' attribute_value )? ';' ;
attribute_name : SCALAR_ID;
attribute_value : (concat_string | concat_number) ;

// eBNF Continued
size : pos_int | '$' SCALAR_ID ;
sized_dec_num : size UNSIZED_DEC_NUM ;
sized_bin_num : size UNSIZED_BIN_NUM ;
sized_hex_num : size UNSIZED_HEX_NUM ;
sized_number : sized_dec_num | sized_bin_num | sized_hex_num;
integer_expr : integer_expr_lvl1 ;
integer_expr_lvl1 : integer_expr_lvl2 ( ('+' | '-') integer_expr_lvl1 )? ;
integer_expr_lvl2 : integer_expr_arg (('*' | '/' | '%') integer_expr_lvl2 )? ;
integer_expr_paren : '(' integer_expr ')'; // Parentheses
integer_expr_arg : integer_expr_paren | pos_int | parameter_ref ;

// eBNF – Lexical 
// Multi-line Comments
ML_COMMENT : '/*' .*? '*/' -> skip ;
// Single-line Comments
SL_COMMENT : '//' (~('\r'|'\n')*) '\r'? '\n' -> skip ;
SCALAR_ID : ('a'..'z' | 'A'..'Z')('a'..'z' | 'A'..'Z' | DEC_DIGIT | '_')* ;
DEC_DIGIT : '0'..'9' ;
UNKNOWN_DIGIT : 'X' | 'x';
BIN_DIGIT : '0'..'1' | UNKNOWN_DIGIT ;
HEX_DIGIT : '0'..'9' | 'A'..'F' | 'a'..'f' | UNKNOWN_DIGIT ;
DEC_BASE : '\'' ('d' | 'D') (' ' | '\t')*;
BIN_BASE : '\'' ('b' | 'B') (' ' | '\t')*;
HEX_BASE : '\'' ('h' | 'H') (' ' | '\t')*;
UNSIZED_DEC_NUM : DEC_BASE POS_INT ;
UNSIZED_BIN_NUM : BIN_BASE BIN_DIGIT('_'|BIN_DIGIT)* ;
UNSIZED_HEX_NUM : HEX_BASE HEX_DIGIT('_'|HEX_DIGIT)* ;
STRING : '"' (~('"'|'\\')|'\\\\'|'\\"')* '"' ;
POS_INT : DEC_DIGIT('_'|DEC_DIGIT)* ;

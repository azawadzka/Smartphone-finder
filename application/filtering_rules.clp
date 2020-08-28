; Rules for release and operatin_system implemented.
; The result is appended to the file "result.txt".
; The rul request_example has examples of requests.

; ref: http://clipsrules.sourceforge.net/documentation/v630/bpg.pdf

;;;;;;;;;;;;
;;PHONES;;;;
;;;;;;;;;;;;
(deftemplate smartphone
  ;operational
  (slot id)
  (slot valid)
  (slot link)
  ;multivaule
	(slot brand)
	(slot model)
  (slot operating_system)
  ;quantitative
  (slot cpu) ;GHz
  (slot memory) ;GB
  (slot ram) ;GB
  (slot camera) ;mpx
  (slot weight) ;g
  (slot screen_diagonal) ;cm
  (slot battery) ;mAh
  (slot price (type FLOAT)) ;euro
  ;binary
  (slot sd) ;y/n
  (slot gps) ;y/n
  (slot bluetooth) ;y/n
  (slot wifi) ;y/n
)

;;;;;;;;;;;;
;;REQUESTS;;
;;;;;;;;;;;;

; HELPER FUNCTION
; https://www.csie.ntu.edu.tw/~sylee/courses/clips/bpg/node12.6.2.html
(deffunction quantitative_operation (?op ?x ?y)
  (if (eq ?op equal)
    then
      (return (= ?x ?y))
    else (if (eq ?op less_than)
      then
        (return (<= ?x ?y))
      else (if (eq ?op more_than)
        then
          (return (>= ?x ?y))
      )
    )
  )
)

;__________________________MULTIVALUE___________________________________

;;; BRAND
(deftemplate request_brand
	(multislot multivalue) ; brands*
)

(defrule rule_brand
  (request_brand (multivalue $?multivalue))
  ?phone <- (smartphone (valid true) (brand ?brand))
  (test (not (member$ ?brand $?multivalue)))
  =>
  (modify ?phone (valid false))
)

;;; MODEL
(deftemplate request_model
	(multislot multivalue) ; models*
)

(defrule rule_model
  (request_model (multivalue $?multivalue))
  ?phone <- (smartphone (valid true) (model ?model))
  (test (not (member$ ?model $?multivalue)))
  =>
  (modify ?phone (valid false))
)

;;; OPERATING SYSTEM
(deftemplate request_operating_system
	(multislot multivalue) ; operating systems*
)

(defrule rule_operating_system
  (request_operating_system (multivalue $?multivalue))
  ?phone <- (smartphone (valid true) (operating_system ?operating_system))
  (test (not (member$ ?operating_system $?multivalue)))
  =>
  (modify ?phone (valid false))
)

;__________________________QUANTITATIVE___________________________________

;;; cpu
(deftemplate request_cpu
	(slot value) ; GHz
	(slot operation) ; operation[equal|less_than|more_than]
)

(defrule rule_cpu
  (request_cpu (value ?value) (operation ?operation))
  ?phone <- (smartphone (valid true) (cpu ?cpu))
  (test (not (quantitative_operation ?operation ?cpu ?value)))
  =>
  (modify ?phone (valid false))
)

;;; MEMORY
(deftemplate request_memory
	(slot value) ; GB
	(slot operation) ; operation[equal|less_than|more_than]
)

(defrule rule_memory
  (request_memory (value ?value) (operation ?operation))
  ?phone <- (smartphone (valid true) (memory ?memory))
  (test (not (quantitative_operation ?operation ?memory ?value)))
  =>
  (modify ?phone (valid false))
)

;;; RAM
(deftemplate request_ram
	(slot value) ; GB
	(slot operation) ; operation[equal|less_than|more_than]
)

(defrule rule_ram
  (request_ram (value ?value) (operation ?operation))
  ?phone <- (smartphone (valid true) (ram ?ram))
  (test (not (quantitative_operation ?operation ?ram ?value)))
  =>
  (modify ?phone (valid false))
)

;;; CAMERA
(deftemplate request_camera
	(slot value) ; mpx
	(slot operation) ; operation[equal|less_than|more_than]
)

(defrule rule_camera
  (request_camera (value ?value) (operation ?operation))
  ?phone <- (smartphone (valid true) (camera ?camera))
  (test (not (quantitative_operation ?operation ?camera ?value)))
  =>
  (modify ?phone (valid false))
)

;;; WEIGHT
(deftemplate request_weight
	(slot value) ; g
	(slot operation) ; operation[equal|less_than|more_than]
)

(defrule rule_weight
  (request_weight (value ?value) (operation ?operation))
  ?phone <- (smartphone (valid true) (weight ?weight))
  (test (not (quantitative_operation ?operation ?weight ?value)))
  =>
  (modify ?phone (valid false))
)

;;; SCREEN_DIAGONAL
(deftemplate request_screen_diagonal
	(slot value) ; cm
	(slot operation) ; operation[equal|less_than|more_than]
)

(defrule rule_screen_diagonal
  (request_screen_diagonal (value ?value) (operation ?operation))
  ?phone <- (smartphone (valid true) (screen_diagonal ?screen_diagonal))
  (test (not (quantitative_operation ?operation ?screen_diagonal ?value)))
  =>
  (modify ?phone (valid false))
)

;;; BATTERY
(deftemplate request_battery
	(slot value) ; mAh
	(slot operation) ; operation[equal|less_than|more_than]
)

(defrule rule_battery
  (request_battery (value ?value) (operation ?operation))
  ?phone <- (smartphone (valid true) (battery ?battery))
  (test (not (quantitative_operation ?operation ?battery ?value)))
  =>
  (modify ?phone (valid false))
)

;;; PRICE
(deftemplate request_price
	(slot value (type FLOAT)) ; euro
	(slot operation) ; operation[equal|less_than|more_than]
)

(defrule rule_price
  (request_price (value ?value) (operation ?operation))
  ?phone <- (smartphone (valid true) (price ?price))
  (test (not (quantitative_operation ?operation ?price ?value)))
  =>
  (modify ?phone (valid false))
)

;_______________________________BINARY___________________________________

;;; SD
(deftemplate request_sd
	(slot has) ; y/n
)

(defrule rule_sd
  (request_sd (has ?has))
  ?phone <- (smartphone (valid true) (sd ?sd))
  (test (not (eq ?sd ?has)))
  =>
  (modify ?phone (valid false))
)

;;; GPS
(deftemplate request_gps
	(slot has) ; y/n
)

(defrule rule_gps
  (request_gps (has ?has))
  ?phone <- (smartphone (valid true) (gps ?gps))
  (test (not (eq ?gps ?has)))
  =>
  (modify ?phone (valid false))
)

;;; BLUETOOTH
(deftemplate request_bluetooth
	(slot has) ; y/n
)

(defrule rule_bluetooth
  (request_bluetooth (has ?has))
  ?phone <- (smartphone (valid true) (bluetooth ?bluetooth))
  (test (not (eq ?bluetooth ?has)))
  =>
  (modify ?phone (valid false))
)

;;; WIFI
(deftemplate request_wifi
	(slot has) ; y/n
)

(defrule rule_wifi
  (request_wifi (has ?has))
  ?phone <- (smartphone (valid true) (wifi ?wifi))
  (test (not (eq ?wifi ?has)))
  =>
  (modify ?phone (valid false))
)


;;;;;;;;;;;;;;;;;;
;;PROGRAM FLOW;;;;
;;;;;;;;;;;;;;;;;;

(defrule print
  (declare (salience -9000))
  (smartphone (valid true) (brand ?brand) (model ?model) (price ?price))
  =>
  ;(printout t ?brand " " ?model " " ?price crlf)
  ;(open "result.txt" F1 "a")
  ;(printout F1 ?brand " " ?model " " ?price crlf)
  ;(close F1)
)


;;; it creates a loop. trying to find a better way to modify
;;; all the smartphones to true, to do a new research without
;;; (reset) _ that is'nt bad at all, in particular if we do it
;;; in the python code

;(defrule allvalid
;  (declare (salience -9999))
;  ?phone <- (smartphone (valid ?tf) (brand ?brand) (model ?model))
;  (test (eq ?tf true))
;  =>
;  (modify ?phone (valid true))
;)


;;;;;;;;;;;;;
;;EXAMPLE;;;;
;;;;;;;;;;;;;

(deffacts request_example
  ;(request_release (value 2018) (operation equal))
  ;(request_operating_system (multivalue "Android"))
)

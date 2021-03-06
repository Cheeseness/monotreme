/*
 ============================================================================
 Name        : SvcApi.h
 Author      : Brad Schoening
 Description : Service definitions for EnergyWise EndPoint API
 ============================================================================

 Copyright (c) 2009-2010 by Cisco Systems, Inc.
*/

/**
 * @file
 * EnergyWise SDK function signatures and descriptions 
 */
#ifndef SVCAPI_H_
#define SVCAPI_H_

#include "EnergyWise.h"

#ifdef __cplusplus
extern "C" {
#endif

/**
 * energywise_svc_status
 *    * DOWN initially
 *    * INITIALIZING when energywise_svc_startup() is called, 
 *      then UP after broadcast of discovery event
 *    * ACTIVE after receiving ACK from discovery broadcast
 */
typedef enum energywise_svc_status {
    SVC_STATUS_ERROR = -1,
    SVC_STATUS_DOWN = 0,	 // Engine is not running, either not started or shutdown
    SVC_STATUS_INITIALIZING = 2, // Engine is starting up
    SVC_STATUS_UP = 1,		 // Engine is up and advertising, but has not received an ACK
    SVC_STATUS_ACTIVE = 3,	 // Engine is up and advertising and has been acknowledged (ACK)
    SVC_STATUS_REQUESTED_SHUTDOWN = 4	// Engine will shutdown at next discovery interval
} energywise_svc_status_t;

/*
 * This section defines function signatures types used in the energywise_svc_registry
 */

typedef int (*service_energywise_next_seqid_type) ();
typedef void (*service_energywise_modified_attribute) (ew_attribute_type_t type);
typedef void (*service_energywise_notify_port) (unsigned short port);

typedef int (*energywise_svc_get_int) ();
typedef int8_t (*energywise_svc_get_int8) ();
typedef uint8_t (*energywise_svc_get_uint8) ();
typedef uint16_t (*energywise_svc_get_uint16) ();
typedef char* (*energywise_svc_get_string) ();
typedef int (*energywise_svc_set_uint8) (uint8_t value);
typedef int (*energywise_svc_fill_int_array) (int* arg);
typedef int (*energywise_svc_fill_ushort_array) (uint16_t* arg);

/**
 * This structure holds callback services for the SDK.  Each callback should be
 * initialized and then the structure passed to energywise_svc_configRegistry.
 */
typedef struct energywise_svc_registry {

    /**
     * These callback functions are used to retrieve the units, usage, caliber,
     * and level information from your system.  They are required by the system
     * and must return back the correct datatype.
     *
     * Additional Note:  These callbacks are issued once for every discovery
     * interval for the system (default 3 minutes), as well as whenever an 
     * EnergyWise query requests them.
     */
    energywise_svc_get_int8 			fn_get_units;
    energywise_svc_get_uint16			fn_get_usage;
    energywise_svc_get_int			fn_get_usageCaliber;
    energywise_svc_get_uint8			fn_get_level;

    /**
     * This callback is used to set the EnergyWise power level on the running
     * system.  It should return -1 on failure or the current level (0..10) on
     * success.
     */
    energywise_svc_set_uint8			fn_set_level;

    /**
     * These callbacks are used to fill in the appropriate vector that has
     * been requested by the system.  The call will provide an address
     * of an already existing array.  Your callback must fill in the array
     * with the corresponding values.
     */
    energywise_svc_fill_ushort_array	        fn_fill_usageVector;
    energywise_svc_fill_int_array		fn_fill_deltaVector;

    /**
     * This callback must supply the system with the next sequence ID to use
     * for the next EnergyWise event.  It is recommended that your application
     * persist the last sequence number so that it can be retrieved in case of
     * restart or system going down.
     */
    service_energywise_next_seqid_type	        energywise_next_seqid;

    /**
     * This callback is provided as a notification to the application that
     * one of the EnergyWise attributes have been modified as a result of
     * and EnergyWise query.  This will notify you which attribute through the 
     * parameter that is passed.
     */
    service_energywise_modified_attribute       energywise_modified_attribute;

    /**
     * This callback is provided to notify the application which TCP listening
     * port has been opened for communication.  This is provided as information
     * in case you must notify any other systems or configure anything else for
     * security (i.e. firewall).
     */
    service_energywise_notify_port              energywise_listen_port;
} energywise_svc_registry_t;

/* forward declaration of internal session structure type */

typedef struct enw_svc_session enw_svc_session_t;


/**
 * Allocates and initializes a session structure and establishes network 
 * configurations.
 *
 * @param[in] *localaddr The local host address in dotted quad notation ("x.x.x.x").
 *
 * @param[in] remote_port The Remote EnergyWise port that the connected switch
 * is configured to run EnergyWise on.  If zero, the default value of IANA
 * 43440 will be used.
 *
 * @param[in] *id A 36-byte EnergyWise ID.  Includes a 32-byte representaiton of 
 * a UUID or Cisco UDI and a 4-byte physical index.
 *
 * @param[in] *key A compiled security key used for authentication that has 
 * been generated using the provided utility function.  Can be NULL if 
 * endpoint security has been set to "security none".
 *
 * @param[in] key_len Length, in bytes, of the uchar* key passed in.  Should be
 * 0 if *key is NULL in case of security none.
 *
 * @param[in] listen_port Optionally specify the local TCP port to listen for
 * EnergyWise events on.  If 0, then the system will choose any available TCP port.
 * 
 * @return session A handle to the structure holding all information used by the
 * SDK to establish and run its internal processing. This is  NULL if an error
 * occured.
 *
 * @usage
 * This must be used to create and initialize the client SDK session.  Note
 * that when endpoint security is set to shared-secret, you must first 
 * generate the security key using the provided utility function.  However,
 * if the endpoint security is set to none, then key should be NULL with
 * key_len set to 0.
 *
 * @codeexample
 * Provide that I already have a UUID and have created a key in variable my_key,
 * create a session with my local ip:port of 10.10.10.1:43440.
 * @code
 * session = energywise_svc_create ("255.255.255.255", 43440, "10.10.10.1", 
 *                                  43440, my_uuid, my_key, key_len);
 * @endcode                             
 */
enw_svc_session_t*
energywise_svc_create(const char* localaddr, const unsigned short remote_port, const energywise_sender_id_t *id, const unsigned char* key, int key_len,
                      const unsigned short listen_port);

/**
 * Configures the identity attributes of the EnergyWise EndPoint
 *
 * @param[in] *session A handle to the structure holding all information 
 * used by the SDK to establish and run its internal processing.
 *
 * @param[in] *domain The EnergyWise domain name.  This must match the domain
 * name of the target switch the SDK is communicating with.
 *
 * @param[in] *name The host devices name.  It is suggested to use the 
 * hostname of the device.
 *
 * @param[in] *role The host devices role.
 *
 * @param[in] *keywords A comma separated list of keywords to be associated
 * with this device.
 * 
 * @param[in] *deviceType The host's device type, e.g. phone.
 *
 * @param[in] importance The host's importance between 1 and 100.
 *
 * @retval 0 Success
 * @retval -1 Failure
 *
 * @usage
 * Use this to initialize the basic attributes associated with this host.
 */
int
energywise_svc_configIdentity(enw_svc_session_t* session, const char* domain, const char* name, const char* role, const char* keywords, const char* deviceType, const uint8_t importance);

/**
 * Configures the callback registry functions.  The passed registry structure 
 * must remain allocated in memory until the discovery engine is shutdown.
 *
 * @param[in] *session A handle to the structure holding all information used by
 * the SDK to establish and run its internal processing.
 *
 * @param[in] *callbackRegistry A pointer to a fully configured registry for the
 * EnergyWise callback functions.
 *
 * @retval 0 Success
 * @retval -1 Failure
 *
 * @usage
 * Use this once you have created the session and setup your callback registry.
 * This must be configured for the function callbacks to work properly.
 *
 * @todo Need code example here
 */
int
energywise_svc_configRegistry(enw_svc_session_t* session, const energywise_svc_registry_t* callbackRegistry);

/**
 * Starts the discovery engine.  This call will not return until the engine
 * is shutdown.
 *
 * @param[in] *session A handle to the structure holding all information used by
 * the SDK to establish and run its internal processing.
 *
 * @retval 0 Success
 * @retval -1 Failure
 *
 * @usage
 * This must be executed to actually startup the service and begin the client.
 */
int
energywise_svc_startup(enw_svc_session_t* session);

/**
 * Posts a request for the engine to shutdown.  The engine will shutdown on or before the next
 * scheduled discovery event broadcast.  Must be called from a different thread than the one
 * that invoked startup.
 *
 * @param[in] *session A handle to the structure holding all information used by
 * the SDK to establish and run its internal processing.
 *
 * @retval 0 Request to shutdown was sent.
 * @retval -1 Request failed, could not send request to shutdown.
 *
 * @usage 
 * This function is to be used when a nice shutdown of the service is desired.
 * It will cause the client to be disconnected from the switch it is connected
 * to.
 */
int
energywise_svc_shutdown(enw_svc_session_t* session);

/**
 * Answer the discovery engine status.  See the status enum for possible values.
 *
 * @param[in] *session A handle to the structure holding all information used by
 * the SDK to establish and run its internal processing.
 *
 * @return  An energywise_svc_status_t enum value indicating the status.
 *
 * @usage
 * Use this when you need to know the current status of the running service.
 */
energywise_svc_status_t
energywise_svc_getStatus(const enw_svc_session_t* session);

/**
 * Set the number of seconds to wait between discovery advertisements once an
 * initial discovery has been ACK-ed.
 *
 * @param[in] *session A handle to the structure holding all information used by
 * the SDK to establish and run its internal processing.
 *
 * @param[in] seconds The number of seconds to wait between updates.
 *
 * @retval 0 Value was set properly
 * @retval -1 Value was not set because it was outside the limits.
 *
 * @usage
 * This is to be used if you would like the client to send updates to the
 * switch more often or less often.  The default is 180 seconds.
 */
int
energywise_svc_setDiscoveryInterval(enw_svc_session_t* session, const int seconds);

/**
 * Get the current value of a particular attribute.
 * 
 * @param[in] *session A handle to the structure holding all information used by
 * the SDK to establish and run its internal processing.
 *
 * @param[in] type An enum value of ew_attribute_type_t specifying the type
 * value requested.
 *
 * @param[out] *length A length variable passed in by the caller.  This will 
 * be set to the length in bytes of the returned pointer to data.
 *
 * @return This function returns a const void pointer to the data requested.
 * The length of data is returned back in the length paramater.  
 *
 * @usage
 * This is to be used if you would like the retrieve the current value of 
 * a given attribute on the running system.  A common example would be to
 * grab the value of all attributes and persist them accross a restart.
 */
const void*
energywise_svc_getAttribute(enw_svc_session_t *session, 
                            ew_attribute_type_t type,
                            int *length);


#ifdef __cplusplus
}
#endif

#endif /* SVCAPI_H_ */
